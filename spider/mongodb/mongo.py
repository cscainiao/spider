
from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017')
# print(client)
db = conn.test

for i in db.collection.find():
    print(i)