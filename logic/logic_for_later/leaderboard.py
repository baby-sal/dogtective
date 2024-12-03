import pygame
import sys
from logic.score_db_connection.db_utils_score import DbClass
from logic.score_db_connection.config import USER, PASSWORD, HOST, DATABASE

class Leaderboard:
    def __init__(self):
        self.db = DbClass(HOST, USER, PASSWORD, DATABASE)

    def display_leaderboard(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if go_back.check_input(mouse_pos_ldr):
                    #     self.menu()
                    pass

            # Fetch leaderboard data from the database
            leaderboard_data = self.db.get_top_ten()

            # Clear screen and display leaderboard
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            y_offset = 50
            if leaderboard_data:
                for row in leaderboard_data:
                    text = font.render(f'{row[0]}: {row[1]}', True, (255, 255, 255))
                    screen.blit(text, (50, y_offset))
                    y_offset += 40

            pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    leaderboard = Leaderboard()
    leaderboard.display_leaderboard()
