#connection and queries
"""
need to install: pip install mysql-connector-python
"""
import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

##Database class

class DbClass(object):

    connection = None

    def __init__(self, host, user, password, database):
        self.host = HOST
        self.user = USER
        self.password = PASSWORD
        self.database = DATABASE

    def db_connect(self):
        if DbClass.connection is None:
            try:
                DbClass.connection = mysql.connector.connect(user = self.user, password = self.password, host = self.host, database = self.host)
            except Exception as an_error:
                print(f"Unable to connect: {an_error}")
            else:
                print("Successfully connected to the database.")

    def get_query(self,sql_query, params=None):
        curs = self.connection.cursor()
        try:
            curs.execute(sql_query,params)
            return curs.fetchall()
        except Exception as an_error:
            print(f"Error executing query {sql_query}: {an_error}")
            return None
        finally:
            curs.close()

    def update_query(self, sql_query, params):
        curs = self.connection.cursor()
        try:
            curs.execute(sql_query, params)
            self.connection.commit()
        except Exception as an_error:
            print(f"Error executing query {sql_query}: {an_error}")
            return None
        finally:
            curs.close()

    def db_disconnect(self):
        if self.connection:
            self.connection.close()
            return f"Disconnected from {self.database}"


## Functions

def get_top_ten():
    database = DbClass(HOST, USER, PASSWORD, DATABASE)
    try:
        database.db_connect()
        sql_query = "SELECT * FROM high_scores"
        result = database.get_query(sql_query)
        return result
    finally:
        database.db_disconnect()

def add_new_score(nickname, score):
    database = DbClass(HOST, USER, PASSWORD, DATABASE)
    try:
        database.db_connect()
        sql_query = f"UPDATE high_scores SET date = CURDATE(), nickname = {nickname}, score = {score}"
        database.update_query(sql_query, nickname, score)
    finally:
        database.db_disconnect()


# if __name__ == "__main__":