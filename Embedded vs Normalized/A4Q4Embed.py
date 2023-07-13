import sys
from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://localhost:{0}".format(sys.argv[1]))

db = client["A4dbEmbed"]

collection = db["SongwritersRecordings"]

query = [{"$match": {"recordings.issue_date": {"$gt": datetime.datetime(1950, 1, 1)}}},
         {"$unwind": "$recordings"},
         {"$project": {"name": "$name", "r_name": "$recordings.name", "r_issue_date": "$recordings.issue_date"}}]

values = collection.aggregate(query)

for value in values:
    print(value)
