import pygame
from user_interface.game_config import WIDTH, HEIGHT
from logic.score_db_connection.db_utils_score import DbClass


class Leaderboard:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font(None, 36)
        self.connection = None
        self.connect_db()

    def connect_db(self):
        DbClass.db_connect()

    def get_scores(self):
       DbClass.get_scores()

    def show(self):
        DbClass.show()


# Example usage
if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dogtective: Leaderboard")
    leaderboard = Leaderboard(display)
    leaderboard.show()
