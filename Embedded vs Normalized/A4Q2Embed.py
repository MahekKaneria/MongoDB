import sys
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:{0}".format(sys.argv[1]))

db = client["A4dbEmbed"]

collection = db["SongwritersRecordings"]

query = [{"$unwind": "$recordings"},
         {"$group": {"_id": "$recordings.recording_id", "rhythmicality": {"$avg": "$recordings.rhythmicality"}}},
         {"$match": {"_id": {"$regex": "^70"}}},
         {"$group": {"_id": "", "avg_rhythmicality": {"$avg": "$rhythmicality"}}}]

values = collection.aggregate(query)

for value in values:
    print(value)
