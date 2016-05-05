import os
from flask import Flask, render_template
from mongomanager import init_pymongo

app = Flask(__name__)

@app.route("/")
def hello():
    return "CoverVote!"

@app.route("/addsong")
def addsong():
	return render_template("SuggestSong.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    init_pymongo(app)
    app.run(debug=True, host='0.0.0.0', port=port)
    
