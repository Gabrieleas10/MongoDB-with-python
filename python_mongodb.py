# importing libs
import datetime
import pymongo
from pymongo import MongoClient

# declaring the port and host of MongoDB
host = 'localhost'
port = 27017

# connecting with MongoDB
client = MongoClient(host = host , port = port)

# show the database list names
print(client.list_database_names())

# choosing database
db = client['loja']

# 
colec = db.test_collection
