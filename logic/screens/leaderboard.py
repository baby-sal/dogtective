import pygame
import sys
from logic.score_db_connection.db_utils_score import DbClass
from logic.score_db_connection.config import HOST, USER, PASSWORD, DATABASE
from user_interface.game_config import WIDTH, HEIGHT  # Correct path to game_config

def leaderboard(self):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.Font(None, 36)

    # Create an instance of DbClass
    db = DbClass(HOST, USER, PASSWORD, DATABASE)

    # Fetch top ten scores from the database
    scores = db.get_top_ten()

    go_back = pygame.Rect(50, 50, 100, 50)

    while True:
        self.display.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_back.collidepoint(event.pos):
                    self.show_menu()

        pygame.draw.rect(self.display, BLACK, go_back)
        back_text = font.render("Go Back", True, WHITE)
        self.display.blit(back_text, (go_back.x + 10, go_back.y + 10))

        title_text = font.render("Leaderboard", True, BLACK)
        self.display.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        # Display scores from the database
        for i, (nickname, score) in enumerate(scores):
            score_text = font.render(f"{nickname}: {score}", True, BLACK)
            self.display.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 100 + i * 40))

        pygame.display.update()
