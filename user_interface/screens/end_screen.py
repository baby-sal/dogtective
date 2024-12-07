import pygame
import sys
from user_interface.screens.screen import Screen
from user_interface.game_config import GameState, WIDTH
from logic.components.button import Button
from logic.components.score import Score
from logic.score_db_connection.db_utils_score import DbClass

class EndScreen(Screen):
    def __init__(self, display, runner):
        super().__init__(display, runner)
        self.db = DbClass()

    def you_win(self):
        health = self.runner.character.health.current
        elapsed_time = self.runner.get_elapsed_time()
        score = Score.calculate_score(health, elapsed_time)
        self.db.add_new_score(score)
        print(f"DB top ten: {self.db.get_top_ten()}")
        print(f"score: {score}")

        while self.runner.current_state == GameState.WIN:
            mouse_pos_complete = pygame.mouse.get_pos()

            self.display.fill("pink")
            bg = pygame.transform.smoothscale(
                pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(),
                self.display.get_size())
            self.display.blit(bg, (0, 0))

            self.image.dogtective_image(WIDTH / 2, 575, self.display)
            self.text.text_blit(f"time spent: {elapsed_time} seconds", 60, "crimson", WIDTH / 2, 400)
            self.text.text_blit(f"health remaining: {health}", 60, "crimson", WIDTH / 2, 450)
            self.button_next_level = Button(image=None, pos_x=WIDTH / 2, pos_y=600, font=self.text.pixel_font(75),
                                            colour="purple4", text_in="Next Level")
            self.text.text_blit("mission complete!", 160, "indigo", WIDTH / 2, 300)

            button_go_back = Button(image=None, pos_x=1100, pos_y=50, font=self.text.pixel_font(40),
                                    colour="purple4", text_in="Menu")

            button_go_back.update_button(self.display)
            self.button_next_level.update_button(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_go_back.check_input(mouse_pos_complete):
                        self.runner.current_state = GameState.MENU
                    if self.button_next_level.check_input(mouse_pos_complete):
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("../logic/assets/audio/BGM_game.mp3")
                        pygame.mixer.music.play(-1)
                        self.runner.current_state = GameState.GAMEPLAY

            pygame.display.update()

    def you_lose(self):
        while self.runner.current_state == GameState.LOSE:
            mouse_pos_end = pygame.mouse.get_pos()
            mouse_pos_play_again = pygame.mouse.get_pos()

            self.display.fill("pink")
            bg = pygame.transform.smoothscale(
                pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(),
                self.display.get_size())
            self.display.blit(bg, (0, 0))


            self.text.text_blit("GAME OVER", 200, "crimson", WIDTH / 2, 300)
            self.image.dogtective_image(WIDTH / 2, 575, self.display)
            self.button_play_again = Button(image=None, pos_x=WIDTH / 2, pos_y=500, font=self.text.pixel_font(75),
                                      colour="purple4", text_in="Play Again")
            button_go_back = Button(image=None, pos_x=1100, pos_y=50, font=self.text.pixel_font(40),
                                    colour="purple4", text_in="Menu")

            button_go_back.update_button(self.display)
            self.button_play_again.update_button(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_go_back.check_input(mouse_pos_end):
                        self.runner.current_state = GameState.MENU
                    if self.button_play_again.check_input(mouse_pos_play_again):
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("../logic/assets/audio/BGM_game.mp3")
                        pygame.mixer.music.play(-1)
                        self.runner.current_state = GameState.GAMEPLAY

            pygame.display.update()
