# importing libs
import pymongo
from pymongo import MongoClient

# declaring the port and host of MongoDB
host = 'localhost'
port = 27017

# connecting with MongoDB
client = MongoClient(host = host , port = port)

print(client.list_database_names())

