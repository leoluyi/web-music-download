import pymongo

client = pymongo.MongoClient(['localhost:27017'])

DATABASE = client['test1']
DATABASE['student'].insert({'name': 'John', 'age': 18, 'height': 188})
DATABASE['student'].remove({'name': 'John'})
