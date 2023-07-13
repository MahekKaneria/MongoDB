import sys
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:{0}".format(sys.argv[1]))

db = client["A4dbNorm"]

recordings = db["recordings"]

query = [{"$unwind": "$songwriter_ids"},
         {"$lookup": {"from": "songwriters","localField": "songwriter_ids","foreignField": "songwriter_id","as": "songwriter"}},
         {"$unwind": "$songwriter"},
         {"$group": {"_id": "$songwriter.songwriter_id","total_length": {"$sum": "$length"}}},
         {'$project': {'_id': 1, 'total_length': '$total_length', 'songwriter_id': '$_id'}}]

results= recordings.aggregate(query)

for result in results: 
    print(result)   

