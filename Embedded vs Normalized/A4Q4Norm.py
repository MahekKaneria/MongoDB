import sys
from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://localhost:{0}".format(sys.argv[1]))

db = client["A4dbNorm"]

collection = db["recordings"]

query = [{"$match": {"issue_date": {"$gt": datetime.datetime(1950, 1, 1)}}},
         {"$lookup": {"from": "songwriters", "localField": "songwriter_ids","foreignField": "songwriter_id", "as": "songwriter"}},
         {"$unwind": "$songwriter"},
         {"$project": {"name": "$songwriter.name", "r_name": "$name", "r_issue_date": "$issue_date"}}]

values = collection.aggregate(query)

for value in values:
    print(value)
