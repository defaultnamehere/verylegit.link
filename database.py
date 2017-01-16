
import datetime
import json
import urllib

import pyrebase

import sketchify
import sketchy_data
import utils


FIREBASE_CONFIG_PATH = "firebase_config.json"


class URLStoreModel():

    def __init__(self):

        with open(FIREBASE_CONFIG_PATH) as f:
            self.config = json.load(f)

        firebase = pyrebase.initialize_app(self.config)

        self.db = firebase.database()
        self.initial_setup()

    def initial_setup(self):
        if not self.db.child("long_urls").get().val():
            for sample_long_url in sketchy_data.SAMPLE_LONG_URLS:
                self.add(sample_long_url)

    def add(self, long_url):
        sketchy_url = sketchify.generate_sketchy_url()
        self.set_url(long_url, sketchy_url)

    @utils.escape_string_args
    def set_url(self, long_url, sketchy_url):

        # Only care about the part after the slash, since we don't care about
        # the domain
        data = {
            "long_url": long_url,
            "sketchy_url": sketchy_url
        }

        self.db.child("long_urls").child(long_url).set(data)
        # If there's a collision this is totally going to overwrite the old value lmao.
        # TODO panic I guess
        self.db.child("sketchy_urls").child(sketchy_url).set(data)
        print(long_url)
        print("Setting (unescaped)" + utils.firebase_unescape(long_url) +
              " -> " + utils.firebase_unescape(sketchy_url))

        print("Setting " + long_url + " -> " + sketchy_url)

    @utils.escape_string_args
    def get_long_url(self, sketchy_url):

        url_data = self.db.child("sketchy_urls").child(sketchy_url).get()

        # None if we don't have this URL already
        if not url_data or not url_data.val():
            #print("Getting: "+  utils.firebase_unescape(sketchy_url) + " -> None")
            return None

        long_url = utils.firebase_unescape(url_data.val()["long_url"])
        #print("Getting: " + utils.firebase_unescape(sketchy_url) + " -> " + utils.firebase_unescape(long_url))
        return long_url

    @utils.escape_string_args
    def get_sketchy_url(self, long_url):

        print(long_url)
        url_data = self.db.child("long_urls").child(long_url).get()

        # None if we don't have this URL already
        if not url_data or not url_data.val():
            print(long_url + " -> None")
            return None

        sketchy_url = utils.firebase_unescape(url_data.val()["sketchy_url"])
        print(long_url + " -> " + sketchy_url)
        return sketchy_url

    def dump(self):
        long_urls = self.db.child("long_urls").get().val()

        dump = {}
        # Unescape the db
        for key, value in long_urls.items():
            #import ipdb; ipdb.set_trace()
            dump[utils.firebase_unescape(key)] = {
                inner_key: utils.firebase_unescape(inner_value)
                for inner_key, inner_value in value.items()}

        print(long_urls)
        with open("dump.json", "w") as f:
            json.dump(dump, f,
                      indent=4, separators=(',', ': '))

    @utils.escape_string_args
    def delete_long(self, key):
        print("Deleting %s as long_url" % key)
        return self.db.child("long_urls").child(key).remove()

    @utils.escape_string_args
    def delete_sketchy(self, key):
        print("Deleting %s as sketchy_url" % key)
        return self.db.child("sketchy_urls").child(key).remove()

    def purge(self, key):
        """Delete this as both a sketchy url and a long one, as well as its counterpart"""
        # See if it has a value as a long url or a sketchy one.

        long_url = self.get_long_url(key)
        sketchy_url = self.get_sketchy_url(key)

        # Delete the whold worrrld.
        print("long, sketchy =", (long_url, sketchy_url))
        if long_url is not None:
            print("Deleting %s as long_url" % long_url)
            self.delete_long(long_url)
            self.delete_sketchy(long_url)

        if sketchy_url is not None:
            self.delete_long(sketchy_url)
            self.delete_sketchy(sketchy_url)
