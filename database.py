
import datetime
import json

import pyrebase


FIREBASE_CONFIG_PATH = "firebase_config.json"

class URLStoreModel():

    def __init__(self):

        with open(FIREBASE_CONFIG_PATH) as f:
            self.config = json.load(f)

        firebase = pyrebase.initialize_app(self.config)

        self.db = firebase.database()

    def set_url(self, long_url, sketchy_url):

        # Only care about the part after the slash, since we don't care about the domain
        data = {
            "long_url": long_url,
            "sketchy_url": sketchy_url,
            "clicks": 0,
            "created": datetime.datetime.utcnow()
        }

        # Set up a mapping both ways.
        self.db.child("urls").child(long_url).set(data)
        self.db.child("urls").child(sketchy_url).set(data)

    def get_long_url(self, sketchy_url):

        url_data = self.db.child("urls").child(sketchy_url).get().val()

        # None if we don't have this URL already
        if not url_data:
            return None


        return url_data["long_url"]

    def get_sketchy_url(self, long_url):

        url_data = self.db.child("urls").child(long_url).get().val()

        # None if we don't have this URL already
        if not url_data:
            return None

        return url_data["sketchy_url"]
