from flask import Flask, jsonify, request
from db_utils_score import get_top_ten, add_new_score
#this might be where we connect the score file from python

app = Flask(__name__)

@app.route("/high-scores", methods=["GET"])
def high_scores():
    return jsonify(get_top_ten())

@app.route("/add_score", methods=["POST"])
def add_score():
    data = request.get_json()
    nickname = data['nickname']
    score = data['score']
    add_new_score(nickname, score)
    return jsonify({"message": "Score added successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
    
#debug outputs: cannot import name 'get_top_ten' from 'db_utils_score'