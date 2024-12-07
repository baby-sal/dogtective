import pygame
import sys

# from logic.score_db_connection.score_connection_to_saving_score_file import score
from user_interface.screens.screen import Screen
from user_interface.game_config import GameState
from logic.components.button import Button
from logic.components.score import Score

class EndScreen(Screen):

    def you_win(self):

        health = self.runner.character.health.current
        elapsed_time = self.runner.get_elapsed_time()
        score = Score.calculate_score(health, elapsed_time)
        print(f"score: {score}")

        while self.runner.current_state == GameState.WIN:
            mouse_pos_complete = pygame.mouse.get_pos()

            self.display.fill("pink")
            bg = pygame.transform.smoothscale(
                pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(),
                self.display.get_size())
            self.display.blit(bg, (0, 0))

            self.text.text_blit("mission complete!", 175, "indigo", 640, 300)
            self.image.dogtective_image(640, 575, self.display)

            button_go_back = Button(image=None, pos_x=1200, pos_y=50, font=self.text.pixel_font(40),
                                    colour="purple4", text_in="go back")

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
        while self.runner.current_state == GameState.LOSE:
            mouse_pos_end = pygame.mouse.get_pos()

            self.display.fill("pink")
            bg = pygame.transform.smoothscale(
                pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(),
                self.display.get_size())
            self.display.blit(bg, (0, 0))

            self.text.text_blit("GAME OVER", 200, "crimson", 640, 300)
            self.image.dogtective_image(640, 575, self.display)

            button_go_back = Button(image=None, pos_x=1200, pos_y=50, font=self.text.pixel_font(40),
                                    colour="purple4", text_in="go back")

            button_go_back.update_button(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_go_back.check_input(mouse_pos_end):
                        self.runner.current_state = GameState.MENU

            pygame.display.update()