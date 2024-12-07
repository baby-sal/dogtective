import pygame
import sys
from user_interface.game_config import WIDTH, HEIGHT, GameState
from logic.components.button import Button
from user_interface.menu_runner import Screen
from logic.score_db_connection.db_utils_score import DbClass


class Leaderboard(Screen):

    def __init__(self, display, runner):
        super().__init__(display, runner)
        self.db = DbClass()
        pygame.display.set_caption("Dogtective: Leaderboard")
        self.background = pygame.image.load(
            "../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background, self.display.get_size())
        self.font = pygame.font.SysFont('comicsansms', 36)

    def show(self):
        scores = self.db.get_top_ten()
        if not scores:
            print("No scores to display.")

        button_go_back = Button(image=None, pos_x=WIDTH - 80, pos_y=50, font=self.text.pixel_font(40), colour="purple4",
                                text_in="go back")

        self.display.blit(self.background, (0, 0))
        self.text.text_blit("leaderboard:", 125, "brown", WIDTH // 2, HEIGHT // 6)
        self.image.dogtective_image(200, 600, self.display)

        # Display scores from the database
        if scores:
            for i, (user_id, score) in enumerate(scores):
                score_text = self.font.render(f"Player {user_id}: {score}", True, "brown")
                self.display.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200 + i * 40))
        else:
            self.text.text_blit("No scores found", 36, "brown", WIDTH // 2, 300)

        while self.runner.current_state == GameState.LEADERBOARD:
            mouse_pos_ldr = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_go_back.check_input(mouse_pos_ldr):
                        self.runner.current_state = GameState.MENU

            button_go_back.update_button(self.display)

            pygame.display.update()


# Example usage
if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dogtective: Leaderboard")
    leaderboard = Leaderboard(display, None)  # Assuming runner instance is passed in the main game logic
    leaderboard.show()
