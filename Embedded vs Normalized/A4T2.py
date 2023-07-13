import sys
from pymongo import MongoClient
from bson.json_util import loads


client = MongoClient("mongodb://localhost:{0}".format(sys.argv[1]))

db = client["A4dbEmbed"]

collection = db["SongwritersRecordings"]
collection.drop()
collection = db["SongwritersRecordings"]

with open("songwriters.json", encoding="utf8") as file:
    songwriters = loads(file.read())

with open("recordings.json", encoding="utf8") as file:
    recordings = loads(file.read())

for songwriter in songwriters:
    for recording in songwriter.get("recordings")[:]:
        songwriter.get("recordings").remove(recording)
        for recording_search in recordings:
            recording_id = recording_search.get("recording_id")
            if recording == recording_id:
                songwriter.get("recordings").append(recording_search)
                break

print("Inserted {0} documents.".format(len(collection.insert_many(songwriters).inserted_ids)))
