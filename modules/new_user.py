from .database import Database


db = Database('localhost:27017', 'project')
db.insert('user')


