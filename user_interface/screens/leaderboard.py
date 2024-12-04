import pygame
import sys
from user_interface.game_config import WIDTH, HEIGHT
from logic.score_db_connection.db_utils_score import DbClass

class Leaderboard:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font(None, 36)
        self.db = DbClass()  # Initialize DbClass instance

    def get_scores(self):
        self.db.db_connect()
        scores = self.db.get_query("SELECT nickname, score FROM high_scores ORDER BY score DESC LIMIT 10")
        self.db.db_disconnect()
        return scores

    def show(self):
        scores = self.get_scores()
        if not scores:
            print("No scores to display.")
            return

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
            for i, (nickname, score) in enumerate(scores):
                score_text = self.font.render(f"{nickname}: {score}", True, self.BLACK)
                self.display.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 100 + i * 40))

            pygame.display.update()

# Example usage
if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dogtective: Leaderboard")
    leaderboard = Leaderboard(display)
    leaderboard.show()
