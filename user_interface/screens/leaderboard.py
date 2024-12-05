import pygame
import sys
import mysql.connector
from user_interface.game_config import WIDTH, HEIGHT, GameState
from logic.score_db_connection.config import USER, PASSWORD, HOST, DATABASE
from logic.components.button import Button
from user_interface.image_loader import Image
from user_interface.text_loader import Text
from user_interface.menu_runner import Screen


class Leaderboard(Screen):

    def __init__(self, display, runner):
        super().__init__(display, runner)
        self.connection = None
        self.connect_db()
        pygame.display.set_caption("Dogtective: Leaderboard")
        self.background = pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha()
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
        self.display.blit(self.background, (0,0))
        self.text.text_blit("leaderboard:", 100, "orange", WIDTH // 2, HEIGHT // 7)
        self.image.dog_walk_image(600, 175, self.display)


        button_go_back = Button(image=None, pos_x=WIDTH - 80, pos_y=50, font=self.text.pixel_font(40), colour="purple4",
                                text_in="go back")
        button_go_back.update_button(self.display)

        if not scores:
            print("No scores to display.")  # Debug statement
        else:
            print(f"Displaying scores: {scores}")  # Debug statement
        go_back = pygame.Rect(50, 50, 100, 50)

        while self.runner.current_state == GameState.LEADERBOARD:
            mouse_pos_ldr = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_go_back.check_input(mouse_pos_ldr):
                        self.runner.current_state = GameState.MENU

            # Display scores from the database
            for i, (user_id, score) in enumerate(scores):
                score_text = self.text.text_blit(f"{user_id}: {score}", 100, "orange", WIDTH // 2, HEIGHT // 7)
                self.display.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 100 + i * 40))

            pygame.display.update()



# Example usage
if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dogtective: Leaderboard")
    leaderboard = Leaderboard(display)
    leaderboard.show()
