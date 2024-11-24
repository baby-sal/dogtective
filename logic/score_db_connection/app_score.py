from flask import Flask, jsonify, request
from db_utils_score import get_top_ten, add_new_score

app = Flask(__name__)

@app.route("/high-scores", methods=["GET"])
def get_high_scores():
    return jsonify(get_top_ten())

@app.route("/add_score", methods=["POST"])
def add_new_score():
    nickname, score = request.get_json()
    return jsonify(add_new_score(nickname,score))

if __name__ == "__main__":
    app.run(debug=True)