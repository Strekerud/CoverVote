#/usr/bin/python
from bson.json_util import dumps
from spotifycommunicator import search_tracks
from mongomanager import add_track_to_db, get_all_tracks

def build_track_json(track,artist=""):
    track_json = search_tracks(track,artist)
    for tracks in track_json:
       tracks["rating"] = 1
    return track_json

def push_to_db(track_json):
   add_track_to_db(track_json)

def get_tracks_from_db():
    return dumps(get_all_tracks())

def get_search_result(track,artist=""):
    return build_track_json(track,artist)
