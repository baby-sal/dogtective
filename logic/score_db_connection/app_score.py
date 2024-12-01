from flask import Flask, jsonify, request
from logic.score_db_connection.db_utils_score import DbClass
from logic.score_db_connection.config import HOST, USER, PASSWORD, DATABASE

app = Flask(__name__)

# Create an instance of DbClass
db = DbClass(HOST, USER, PASSWORD, DATABASE)

@app.route("/high-scores", methods=["GET"])
def high_scores():
    return jsonify(db.get_top_ten())

@app.route("/add_score", methods=["POST"])
def add_score():
    data = request.get_json()
    nickname = data['nickname']
    score = data['score']
    db.add_new_score(nickname, score)
    return jsonify({"message": "Score added successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
