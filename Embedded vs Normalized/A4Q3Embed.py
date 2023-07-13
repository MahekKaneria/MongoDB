import sys
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:{0}".format(sys.argv[1]))

db = client["A4dbEmbed"]

collection = db["SongwritersRecordings"]

query=[{'$unwind': '$recordings'},
       {'$group': {'_id': '$songwriter_id', 'total_length': {'$sum': '$recordings.length'}}},
       {'$project': {'total_length': 1, 'songwriter_id': '$_id'}}]

results = collection.aggregate(query)

for result in results:
    print(result)
