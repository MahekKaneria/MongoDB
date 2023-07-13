import sys
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:{0}".format(sys.argv[1]))

db = client["A4dbEmbed"]

collection = db["SongwritersRecordings"]

query = [{"$project": {"_id": 1, "songwriter_id": 1, "name": 1, "num_recordings": {"$size": "$recordings"}}},
         {"$match": {"num_recordings": {"$gt": 0}}}]

values = collection.aggregate(query)

for value in values:
    print(value)
