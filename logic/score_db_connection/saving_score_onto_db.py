import sqlite3  # SQLite database module
from datetime import datetime  # Module to handle date and time
from logic.score_db_connection.db_utils_score import DbClass

class SavingScoreOntoDB:
    def __init__(self, db_path):
        self.db = DbClass()  # Initialize DbClass instance
        self.db_path = db_path
        # Connect to the SQLite database with thread safety turned off
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        # Create the high_scores table if it doesn't exist
        self._create_table()

    def _create_table(self):
        # Call the method from DbClass to create the table
        self.db._create_table()

    def add_new_score(self, nickname, score):
        # Insert new score using DbClass
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.add_new_score(nickname, score)

    def get_top_ten(self):
        # Get top ten scores using DbClass
        return self.db.get_top_ten()

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_path = 'logic.score_db_connection.dogtective_scores_db.sql'  # Make sure to update this path to where your database is stored
    db = SavingScoreOntoDB(db_path)
    db.add_new_score("PlayerOne", 1234)  # Example of adding a new score
    top_ten_scores = db.get_top_ten()  # Fetching top ten scores
    print(top_ten_scores)  # Print the top ten scores
    db.close_connection()  # Close the database connection
