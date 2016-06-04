import os

from flask import Flask, render_template, request, jsonify, redirect
from covervoteservice import push_to_db, get_tracks_from_db, get_search_result
from bson.json_util import loads

app = Flask(__name__)

search_result = []

@app.route("/")
def index():
    return render_template("index.html", tracks=loads(get_tracks_from_db()), search_result=search_result)

@app.route("/submitsong", methods=["POST"])
def submitsong():
    global search_result
    search_result = []
    artist = request.form['artist']
    song = request.form['song']
    search_result = get_search_result(song,artist)
    return redirect("/")
        
@app.route("/tracks")
def get_all_tracks():
    return get_tracks_from_db()

@app.route("/1")
def add_song_1():
    global search_result
    push_to_db(search_result[0])
    search_result = []
    return redirect("/")
    
@app.route("/2")
def add_song_2():
    global search_result
    push_to_db(search_result[1])
    search_result = []
    return redirect("/")
                      
@app.route("/3")
def add_song_3():
    global search_result
    push_to_db(search_result[2])
    search_result = []
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

    
