import pygame
import sys

from user_interface.screens.screen import Screen
from user_interface.game_config import GameState, WIDTH
from logic.components.score import Score
from logic.components.button import Button
from logic.score_db_connection.db_utils_score import DbClass

from logic.components.timer import Timer

class EndScreen(Screen):
    def __init__(self, display, runner):
        super().__init__(display, runner)
        self.db = DbClass()

    def you_win(self):
        health = self.runner.character.health.current
        elapsed_time = self.runner.get_elapsed_time()
        score = Score.calculate_score(health, elapsed_time)
        self.db.add_new_score(score)

        self.display.fill("pink")
        bg = pygame.transform.smoothscale(
            pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(),
            self.display.get_size())
        self.display.blit(bg, (0, 0))

        self.text.text_blit("mission complete!", 160, "indigo", WIDTH / 2, 150)
        self.text.number_blit(f"Score: {str(score)}", 100, "indigo", WIDTH / 2, 275)
        self.text.number_blit(f"time: {elapsed_time}s", 60, "crimson", WIDTH/2, 400)
        self.text.number_blit(f"bones left: {health}", 60, "crimson", WIDTH/2, 450)
        self.image.dogtective_image(5 * WIDTH / 6, 575, self.display)

        button_go_back = Button(image=None, pos_x=1100, pos_y=50, font=self.text.pixel_font(40),
                                colour="purple4", text_in="Menu")

        while self.runner.current_state == GameState.WIN:
            mouse_pos_complete = pygame.mouse.get_pos()

            button_go_back.update_button(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_go_back.check_input(mouse_pos_complete):
                        self.runner.current_state = GameState.MENU

            pygame.display.update()

    def you_lose(self):

        self.display.fill("pink")
        bg = pygame.transform.smoothscale(
            pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(),
            self.display.get_size())
        self.display.blit(bg, (0, 0))

        self.text.text_blit("GAME OVER", 200, "crimson", WIDTH / 2, 300)
        self.image.dogtective_image(WIDTH / 2, 575, self.display)

        button_go_back = Button(image=None, pos_x=1100, pos_y=50, font=self.text.pixel_font(40),
                                colour="purple4", text_in="Menu")

        while self.runner.current_state == GameState.LOSE:
            mouse_pos_end = pygame.mouse.get_pos()

            button_go_back.update_button(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_go_back.check_input(mouse_pos_end):
                        self.runner.current_state = GameState.MENU

            pygame.display.update()
