import sys
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:{0}".format(sys.argv[1]))

db = client['A4dbNorm']

recordings = db['recordings']

query = [{"$match": {"recording_id": {"$regex": "^70"}}},
         {"$group": {"_id": "", "avg_rhythmicality": {"$avg": "$rhythmicality"}}}]

results = recordings.aggregate(query)

for result in results:
    print(result)
