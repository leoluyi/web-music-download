# MongoDB basics

1. Run `$ mongod [--dbpath arg]`
2. Use CLI `$ mongo`

```
show dbs
show collection

use <db_name> # Switch db or create new db
db.<collection>.insert(<json_string>) # Insert data

db.<collection>.find()
db.<collection>.find().pretty()       # Pretty format
db.<collection>.delete(<json_mapping>)

db.DropDatabase
``
