import pymongo


class Database(object):
    """MongoDB database"""

    URI = ['localhost:27017']
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['project']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        Database.DATABASE[collection].find_one(query)
