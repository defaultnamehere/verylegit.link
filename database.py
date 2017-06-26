
import sketchify
import sketchy_data
import random

from google.cloud import datastore


class URLStoreModel():

    def __init__(self):


        datastore_client = datastore.Client(
            project="verylegitlink")
        self.db = datastore_client
        # self.initial_setup()

    def initial_setup(self):
        if not self.get_sketchy_url(random.choice(sketchy_data.SAMPLE_LONG_URLS)):
            for sample_long_url in sketchy_data.SAMPLE_LONG_URLS:
                self.add(sample_long_url)

    def add(self, long_url):
        sketchy_url = sketchify.generate_sketchy_url()
        self.set_url(long_url, sketchy_url)

    def set_url(self, long_url, sketchy_url):

        with self.db.transaction():
            incomplete_key = self.db.key("URL")
            url = datastore.Entity(key=incomplete_key)
            url.update({
                "long_url": long_url,
                "sketchy_url": sketchy_url
            })
            self.db.put(url)

        print("Setting " + long_url + " -> " + sketchy_url)

    def get_long_url(self, sketchy_url):

        query = self.db.query(kind="URL")
        query.add_filter("sketchy_url", "=", sketchy_url)

        result = list(query.fetch(limit=1))

        # None if we don't have this URL already
        if not result:
            print("Getting: " + sketchy_url + " -> " + str(result))
            return None

        long_url = result[0]["long_url"]
        return long_url

    def get_sketchy_url(self, long_url):

        query = self.db.query(kind="URL")
        query.add_filter("long_url", "=", long_url)

        result = list(query.fetch(limit=1))

        print(result)
        if not result:
            print("Getting: " + long_url + " -> None")
            return None

        sketchy_url = result[0]["sketchy_url"]

        return sketchy_url

if __name__ == "__main__":
    URLStoreModel().initial_setup()
