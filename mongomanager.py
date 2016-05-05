#/usr/bin/python
from pymongo import MongoClient


client = MongoClient('mongodb://covervote:covervote12@ds013202.mlab.com:13202/heroku_w60qmjwf')
#LOKAL: client = MongoClient()
db = client.covervote
collection = db.tracks


def add_track_to_db(track_json):
    collection.insert_one(track_json)
    
#def add_point(spotify_id):
#   track = collection.find_one({"spotify_id": spotify_id})
#  collection.update_one({"spotify_id": spotify_id,
#                           {"$inc": { "rating": 1}})
        
#def deduct_point(spotify_id):
  
    
def get_track_from_db(track_json):
    if db_contains_track(track_json):
        return collection.find_one(track_json)
    else:
        #return track not found error or something
        return null
    
def db_contains_track(track_json):
    if collection.find_one(track_json):
        return True
    else:
        return False
