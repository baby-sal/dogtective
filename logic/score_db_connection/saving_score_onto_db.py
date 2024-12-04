import sqlite3
from datetime import datetime
import os

class DbClass:
    def __init__(self, db_path='dogtective_scores_db.sql'):
        self.db_path = db_path
        if os.path.exists(self.db_path):
            try:
                sqlite3.connect(self.db_path).execute("PRAGMA quick_check")
            except sqlite3.DatabaseError:
                os.remove(self.db_path)
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS high_scores (
                               user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                               date TEXT,
                               nickname TEXT,
                               score INTEGER NOT NULL)''')
        self.conn.commit()

    def add_new_score(self, nickname, score):
        self.cursor.execute('''INSERT INTO high_scores (date, nickname, score) VALUES (?, ?, ?)''',
                            (datetime.now().strftime('%Y-%m-%d'), nickname, score))
        self.conn.commit()

    def get_top_ten(self):
        self.cursor.execute('''SELECT * FROM high_scores ORDER BY score DESC LIMIT 10''')
        return self.cursor.fetchall()
