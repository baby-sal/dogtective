#connection and queries
"""
need to install: pip install mysql-connector-python
"""
import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

##Database class

class DbClass(object):

    connection = None

    def __init__(self, HOST, USER, PASSWORD, DATABASE):
        self.host = HOST
        self.user = USER
        self.password = PASSWORD
        self.database = DATABASE
        #as these are all set to empty string it prevents this file from running, so can't show what it does

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


    def get_top_ten(self):
        self.db_connect()
        try:
            sql_query = "SELECT name, score FROM high_scores ORDER BY score LIMIT 10"
            return self.get_query(sql_query)
        finally:
            self.db_disconnect()

    def add_new_score(self, nickname, score):
        self.db_connect()
        try:
            sql_query = "INSERT INTO high_scores (date, nickname, score) VALUES (CURRENT_DATE(), %s, %s)"
            self.update_query(sql_query, nickname, score)
        finally:
            self.db_disconnect()
            

