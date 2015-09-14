
from flask import Flask, render_template, request, abort

import database
import sketchify

app = Flask('heapslegit')
db = database.URLStoreModel()

@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/sketchify', methods=["POST"])
def sketchify_url(): 
    long_url = request.form.to_dict().get("long_url")
    if long_url is None:
        return abort(401)

    # Try and just get this URL out of the database I mean it might already be there might as well go fishing
    sketchy_url = db.get_sketchy_url(long_url)

    # Okay fine it wasn't there thanks obama
    if sketchy_url is None:

        # Screw the rules we'll make our own URL
        sketchy_url = sketchify.URLSketchifer(long_url).generate_sketchy_url()

        # Save it to the database FO' LATAHZ
        db.set_url(long_url, sketchy_url)

    # Here you go have your url ya nerd
    return sketchy_url

@app.errorhandler(404)
def custom404(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
