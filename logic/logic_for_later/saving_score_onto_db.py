import os
import sqlite3
from datetime import datetime

# Path to the database
DB_PATH = '../logic/score_db_connection.dogtective_scores_db.sql'

# Ensure the directory exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Create a connection to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, score INTEGER, timestamp TEXT)''')
conn.commit()

def save_score_to_db(score):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO scores (score, timestamp) VALUES (?, ?)", (score, timestamp))
    conn.commit()
