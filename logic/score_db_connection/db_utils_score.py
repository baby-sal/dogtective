import mysql.connector
from logic.score_db_connection.config import USER, PASSWORD, HOST, DATABASE
import pygame
import sys
from user_interface.game_config import WIDTH

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
                DbClass.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
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
            sql_query = "SELECT name, score FROM high_scores ORDER BY score LIMIT 10"
            return self.get_query(sql_query)
        finally:
            self.db_disconnect()

    def add_new_score(self, nickname, score):
        self.db_connect()
        try:
            sql_query = "INSERT INTO high_scores (date, nickname, score) VALUES (CURRENT_DATE(), %s, %s)"
            self.update_query(sql_query, (nickname, score))
        finally:
            self.db_disconnect()

    def get_scores(self):
        if self.connection is None:
            print("Database connection is not established.")
            return []

        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT nickname, score FROM high_scores ORDER BY score DESC LIMIT 10")
            scores = cursor.fetchall()
            print(f"Fetched scores: {scores}")  # Debug statement
            return scores
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            cursor.close()

    def show(self):
        scores = self.get_scores()
        if not scores:
            print("No scores to display.")  # Debug statement
        else:
            print(f"Displaying scores: {scores}")  # Debug statement
        go_back = pygame.Rect(50, 50, 100, 50)

        while True:
            self.display.fill(self.WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if go_back.collidepoint(event.pos):
                        return  # Return to break out of the loop and go back to menu

            pygame.draw.rect(self.display, self.BLACK, go_back)
            back_text = self.font.render("Go Back", True, self.WHITE)
            self.display.blit(back_text, (go_back.x + 10, go_back.y + 10))

            title_text = self.font.render("Leaderboard", True, self.BLACK)
            self.display.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

            # Display scores from the database
            for i, (name, score) in enumerate(scores):
                score_text = self.font.render(f"{name}: {score}", True, self.BLACK)
                self.display.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 100 + i * 40))

            pygame.display.update()
