import pygame
import sys
import mysql.connector
from user_interface.game_config import WIDTH, HEIGHT
from logic.score_db_connection.config import USER, PASSWORD, HOST, DATABASE


class Leaderboard:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font(None, 36)
        self.connection = None
        self.connect_db()
        pygame.display.set_caption("Dogtective: Main Menu")
        self.background = pygame.image.load("../logic/assets/images/menu/city_backgroud.png").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background, self.display.get_size())

    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(
                user=USER,
                password=PASSWORD,
                host=HOST,
                database=DATABASE
            )
            if self.connection.is_connected():
                print("Successfully connected to the database.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None

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
            for i, (user_id, score) in enumerate(scores):
                score_text = self.font.render(f"Player {user_id}: Score {score}", True, self.BLACK)
                self.display.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 100 + i * 40))

            pygame.display.update()


# Example usage
if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dogtective: Leaderboard")
    leaderboard = Leaderboard(display)
    leaderboard.show()
