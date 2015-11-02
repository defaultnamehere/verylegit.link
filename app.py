
from flask import Flask, render_template, request, abort, redirect
import random

import database
import sketchify
import sketchy_data
import validate

import urllib


app = Flask('heapslegit')
db = database.URLStoreModel()

@app.route('/')
def index():
    sample_long_url = random.choice(sketchy_data.SAMPLE_LONG_URLS)
    sample_sketchy_url = sketchify.add_random_domain(db.get_sketchy_url(sample_long_url))
    return render_template("index.html", sample_long_url=sample_long_url, sample_sketchy_url=sample_sketchy_url)

@app.route('/sketchify', methods=["POST"])
def sketchify_url(): 
    long_url = request.form.to_dict().get("long_url")
    if long_url is None:
        return abort(401)

    # So you'd like to submit this URL.
    # Let's just make sure you're not trying to 360 noscope hack somebody first.
    validator = validate.URLValidator(long_url)
    if not validator.validate_url():
        return abort(401)


    # Add a http:// if a protocol isn't present.
    if not(long_url.startswith("http://") or long_url.startswith("https://")):
        long_url = "http://" + long_url

    # Try and just get this URL out of the database I mean it might already be there might as well go fishing
    sketchy_url = db.get_sketchy_url(long_url)

    # Okay fine it wasn't there thanks obama
    if sketchy_url is None:

        sketchifier = sketchify.URLSketchifer(long_url)

        # Generate a random URL we don't have yet.
        # Techinically this function may never return.
        while True:
            # Screw the rules we'll make our own URL
            sketchy_url = sketchifier.generate_sketchy_url()
            if db.get_long_url(sketchy_url) is None:
                # This url is unique and we don't need to re-generate
                break

        # Save it to the database FO' LATAHZ
        db.set_url(long_url, sketchy_url)

    # Here you go have your url ya nerd
    return "{proto}{domain}/{path}".format(proto=random.choice(("http://", "")), domain=random.choice(sketchy_data.DOMAINS), path=sketchy_url)


@app.route('/<sketchy_extension>', methods=["GET"])
def redirect_to_sketchy_url(sketchy_extension):

    sketchy_extension = urllib.quote(sketchy_extension)
    # Get the long url for this short url.
    long_url = db.get_long_url(sketchy_extension)
    print("{sketchy_extension} -> {long_url}".format(sketchy_extension=sketchy_extension,
                                                     long_url=long_url))
    if long_url is None:
        return abort(404)

    return redirect(long_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
