
import datetime

# Literally WiredTiger
# I once found a bug in WiredTiger in which you couldn't store 32-bit ints. You just couldn't do it.
import pymongo


class URLStoreModel():

    def __init__(self):
        # Set up connection to the database.
        self.client = pymongo.MongoClient('localhost', 27017)
        self.url_database = self.client.urls
        self.url_collection = self.url_database.urls

    def set_url(self, long_url, sketchy_url):

        # Only care about the part after the slash, since we don't care about the domain
        document = {
            "long_url" : long_url,
            "sketchy_url": sketchy_url,
            "clicks": 0,
            "created": datetime.datetime.utcnow()
        }

        self.url_collection.insert_one(document)

    def get_long_url(self, sketchy_url):

        url_document = self.url_collection.find_one({
            "sketchy_url": sketchy_url
        })

        # None if we don't have this URL already
        if url_document is None:
            return None

        url_id = url_document["_id"]

        # Increment the clicks
        self.url_collection.update_one({'_id': url_id}, {'$inc': {'clicks': 1}})

        return url_document["long_url"]

    def get_sketchy_url(self, long_url):

        url_document = self.url_collection.find_one({
            "long_url": long_url 
        })

        # None if we don't have this URL already
        if url_document is None:
            return None

        return url_document["sketchy_url"]
