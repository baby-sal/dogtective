import sys
import pygame
from logic.components.button import Button
from user_interface.screens.screen import Screen
from user_interface.game_config import GameState, WIDTH


class MenuRunner(Screen):

    def __init__(self, display, runner):
        super().__init__(display, runner)
        self.background = pygame.image.load("../logic/assets/images/menu/city_backgroud.png").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background, self.display.get_size())

    def menu_runner(self):

        while self.runner.current_state == GameState.MENU:
            self.display.blit(self.background, (0, 0))
            mouse_pos_menu = pygame.mouse.get_pos()
            pygame.display.set_caption("Dogtective: Main Menu")

            self.text.text_blit("Dogtective", 200, "royalblue4", WIDTH / 2, 125)
            self.text.text_blit("MAIN MENU", 100, "royalblue4", WIDTH / 2, 250)
            self.image.dog_walk_image(WIDTH / 2, 650, self.display)

            button_play = Button(image=None, pos_x=WIDTH / 2, pos_y=350, font=self.text.pixel_font(75), colour="brown",
                                 text_in="play")
            button_ldr = Button(image=None, pos_x=WIDTH / 2, pos_y=425, font=self.text.pixel_font(75),
                                colour="lightsalmon", text_in="LEADERBOARD")
            button_credits = Button(image=None, pos_x=WIDTH / 2, pos_y=500, font=self.text.pixel_font(75),
                                    colour="lightsalmon", text_in="CREDITS")

            for button in [button_play, button_ldr, button_credits]:
                button.update_button(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_play.check_input(mouse_pos_menu):
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("../logic/assets/audio/BGM_game.mp3")
                        pygame.mixer.music.play(-1)
                        self.runner.current_state = GameState.GAMEPLAY
                    if button_ldr.check_input(mouse_pos_menu):
                        self.runner.current_state = GameState.LEADERBOARD
                    if button_credits.check_input(mouse_pos_menu):
                        self.runner.current_state = GameState.CREDITS
            pygame.display.update()
