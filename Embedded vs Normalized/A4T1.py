import sys
from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient("mongodb://localhost:{0}".format(sys.argv[1]))

db = client['A4dbNorm']

songwriters_collection = db['songwriters']
recordings_collection = db['recordings']

with open("songwriters.json", encoding="utf8") as file:
    songwriters = loads(file.read())

with open("recordings.json", encoding="utf8") as file:
    recordings = loads(file.read())

songwriters_collection.insert_many(songwriters)
recordings_collection.insert_many(recordings)
