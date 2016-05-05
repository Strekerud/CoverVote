import os

from flask import Flask, render_template, request, jsonify
from covervoteservice import push_to_db, get_tracks_from_db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addsong")
def addsong():
	return render_template("SuggestSong.html")

@app.route("/submitsong", methods=["POST"])
def submitsong():
	artist = request.form['artist']
	song = request.form['song']
	push_to_db(song,artist)
        return render_template("index.html")

@app.route("/tracks")
def get_all_tracks():
    return flask.jsonify(**get_tracks_from_db())
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    
