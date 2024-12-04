import sqlite3  # SQLite database module
from datetime import datetime  # Module to handle date and time
import os  # Module to handle file system operations

class DbClass:
    def __init__(self, db_path='dogtective_scores_db.sql'):
        # Initialize the database path and check if the database file exists
        self.db_path = db_path
        if os.path.exists(self.db_path):
            try:
                # Try to connect to the database and run a quick check
                sqlite3.connect(self.db_path).execute("PRAGMA quick_check")
            except sqlite3.DatabaseError:
                # If there's a database error, remove the corrupt database file
                os.remove(self.db_path)
        # Connect to the SQLite database with thread safety turned off
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        # Create the high_scores table if it doesn't exist
        self._create_table()

    def _create_table(self):
        # Create a table named high_scores with columns for user_id, date, nickname, and score
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS high_scores (
                               user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                               date TEXT,
                               nickname TEXT,
                               score INTEGER NOT NULL)''')
        self.conn.commit()

    def add_new_score(self, nickname, score):
        # Add a new score to the high_scores table with the current date, given nickname, and score
        self.cursor.execute('''INSERT INTO high_scores (date, nickname, score) VALUES (?, ?, ?)''',
                            (datetime.now().strftime('%Y-%m-%d'), nickname, score))
        self.conn.commit()

    def get_top_ten(self):
        # Retrieve the top 10 scores from the high_scores table, ordered by score in descending order
        self.cursor.execute('''SELECT * FROM high_scores ORDER BY score DESC LIMIT 10''')
        return self.cursor.fetchall()
