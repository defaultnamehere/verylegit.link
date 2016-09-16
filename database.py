
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

        # Only care about the part after the slash, since we don't care about the domain
        data = {
            "long_url": long_url,
            "sketchy_url": sketchy_url
        }

        self.db.child("long_urls").child(long_url).set(data)
        self.db.child("sketchy_urls").child(sketchy_url).set(data)

    @utils.escape_string_args
    def get_long_url(self, sketchy_url):

        url_data = self.db.child("sketchy_urls").child(sketchy_url).get()

        # None if we don't have this URL already
        if not url_data:
            return None


        return utils.firebase_unescape(url_data.val()["long_url"])

    @utils.escape_string_args
    def get_sketchy_url(self, long_url):

        url_data = self.db.child("long_urls").child(long_url).get()

        # None if we don't have this URL already
        if not url_data or not url_data.val():
            return None

        return utils.firebase_unescape(url_data.val()["sketchy_url"])
