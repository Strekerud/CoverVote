#/usr/bin/python
from spotifycommunicator import get_track
from mongomanager import add_track_to_db

def build_track_json(track,artist=""):
    track_json = get_track(track,artist)
    track_json["rating"] = 1
    return track_json

def push_to_db(track,artist=""):
    add_track_to_db(build_track_json(track,artist))


