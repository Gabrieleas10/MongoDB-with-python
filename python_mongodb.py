# importing libs
import json
import pymongo
from pymongo import MongoClient

# declaring the port and host of MongoDB
host = 'localhost'
port = 27017

# connecting with MongoDB
client = MongoClient(host = host , port = port)

# show the database list names
print(client.list_database_names())

# create database -- its available
db = client['STORE']

# creating collections
colec = db['products']

# json file path
json_file = 'E:\\Projects\\MongoDB-with-python\\data_input.json'

# inserting many values in STORE MongoDB DataBase
with open(json_file) as file: 
    file_data = json.load(file)
    colec.insert_many(file_data['products']).inserted_ids

# showing documents and objects
for x in colec.find():
  print(x)
   





