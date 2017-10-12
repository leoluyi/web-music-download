import pymongo


class Database(object):
    """MongoDB database"""

    def __init__(self, URI='localhost:27017', db, **kwargs):
        '''Initialize MongoDB connection.

        Args:
            URI (str): mongodb connection URI
            **kwargs: Other arguments passed to pymongo.MongoClient

        Check MongoDB connection string
        http://api.mongodb.com/python/current/examples/authentication.html#scram-sha-1-rfc-5802
        '''

        client = pymongo.MongoClient(URI, **kwargs)
        self.db = client[db]

    def insert(self, collection, data):
        self.db[collection].insert(data)

    def find(self, collection, query):
        self.db[collection].find(query)

    def find_one(self, collection, query):
        self.db[collection].find_one(query)
