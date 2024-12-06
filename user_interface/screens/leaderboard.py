import pygame
import sys
from user_interface.game_config import WIDTH, HEIGHT, GameState
from logic.components.button import Button
from user_interface.image_loader import Image
from user_interface.text_loader import Text
from user_interface.menu_runner import Screen
from logic.score_db_connection.db_utils_score import DbClass

class Leaderboard(Screen):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, display, runner):
        super().__init__(display, runner)
        self.connection = None
        self.db = DbClass()
        pygame.display.set_caption("Dogtective: Leaderboard")
        self.background = pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background, self.display.get_size())
        self.text = Text(display)
        self.image = Image()
        self.font = pygame.font.Font(None, 36)#initialise font attribute

    def show(self):
        scores = self.db.get_top_ten()
        if not scores:
            print("No scores to display.")
            return

        while self.runner.current_state == GameState.LEADERBOARD:
            mouse_pos_ldr = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_go_back.check_input(mouse_pos_ldr):
                        self.runner.current_state = GameState.MENU

            self.display.blit(self.background, (0, 0))
            self.text.text_blit("leaderboard:", 125, "brown", WIDTH // 2, HEIGHT // 6)
            self.image.dogtective_image(600, 600, self.display)

            button_go_back = Button(image=None, pos_x=WIDTH - 80, pos_y=50, font=self.text.pixel_font(40), colour="purple4",
                                    text_in="go back")
            button_go_back.update_button(self.display)

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
    leaderboard = Leaderboard(display, None)  # Assuming runner instance is passed in the main game logic
    leaderboard.show()
