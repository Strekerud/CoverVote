import os
from flask import Flask, render_template, request

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
	url = request.form['URL']
	album = request.form['album']
	return request.form['artist']

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
