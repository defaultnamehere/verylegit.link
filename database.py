
import datetime

import pymongo


# Uhh okay we're going to need to choose a database.
# Probably wiredtiger I mean mongo?
class URLStoreModel():

    def __init__(self):
        # Set up connection to the database.
        self.client = pymongo.MongoClient('localhost', 27017)
        self.url_database = self.client.urls
        self.url_collection = self.url_database.urls

    def set_url(self, long_url, sketchy_url):
        document = {
            "long_url" : long_url,
            "sketchy_url": sketchy_url,
            "clicks": 0,
            "created": datetime.datetime.utcnow()
        }
        self.url_collection.insert_one(document)

    def get_sketchy_url(self, long_url):

        url_document = self.url_collection.find_one({
            "long_url": long_url
        })

        # None if we don't have this URL already
        if url_document is None:
            return None

        url_id = url_document["_id"]

        # Increment the clicks
        self.url_collection.update_one({'_id': url_id}, {'$inc': {'clicks': 1}})

        return url_document["sketchy_url"]

