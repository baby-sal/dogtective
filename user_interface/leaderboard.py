import pygame
import sys
from logic.score_db_connection.db_utils_score import DbClass  # Import the DbClass from your connector module
import logic.score_db_connection.config as config
from user_interface.game_config import WIDTH

class Leaderboard:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font(None, 36)

        # Initialize DbClass with connection parameters
        self.db = DbClass()

    def get_scores(self):
        scores = self.db.get_top_ten()
        if scores is None:
            print("Failed to retrieve scores. Check database connection.")
            scores = []
        return scores

    def show(self):
        scores = self.get_scores()
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


# Example usage
if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("Dogtective: Leaderboard")
    leaderboard = Leaderboard(display)
    leaderboard.show()
