import mysql.connector
from logic.score_db_connection.config import USER, PASSWORD, HOST, DATABASE


class DbClass(object):
    connection = None

    def __init__(self):
        self.user = USER
        self.password = PASSWORD
        self.host = HOST
        self.database = DATABASE

    def db_connect(self):
        if DbClass.connection is None:
            try:
                DbClass.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host,
                                                             database=self.database)
                if DbClass.connection.is_connected():
                    print("Successfully connected to the database.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                DbClass.connection = None

    def get_query(self, sql_query, params=None):
        if DbClass.connection is None:
            self.db_connect()
            if DbClass.connection is None:
                return None  # Connection failed
        curs = DbClass.connection.cursor()
        try:
            curs.execute(sql_query, params)
            return curs.fetchall()
        finally:
            curs.close()

    def update_query(self, sql_query, params):
        if DbClass.connection is None:
            self.db_connect()
            if DbClass.connection is None:
                return None  # Connection failed
        curs = DbClass.connection.cursor()
        try:
            curs.execute(sql_query, params)
            DbClass.connection.commit()
        except Exception as an_error:
            print(f"Error executing query {sql_query}: {an_error}")
            return None
        finally:
            curs.close()

    def db_disconnect(self):
        if DbClass.connection:
            DbClass.connection.close()
            DbClass.connection = None
            print(f"Disconnected from {self.database}")

    def get_top_ten(self):
        self.db_connect()
        try:
            sql_query = "SELECT user_id, score FROM high_scores ORDER BY score DESC LIMIT 10"
            return self.get_query(sql_query)
        finally:
            self.db_disconnect()

    def add_new_score(self, score):
        self.db_connect()
        try:
            sql_query = "INSERT INTO high_scores (date, score) VALUES (CURRENT_DATE(), %s)"
            self.update_query(sql_query, [score])
        finally:
            self.db_disconnect()


if __name__ == "__main__":
    pass
