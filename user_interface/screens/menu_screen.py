from logic.components.button import Button
from user_interface.game import run
import pygame


def __init__(self):
    pygame.init()
    self.display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("Dogtective: Main Menu")
    self.background = pygame.image.load("../logic/assets/images/menu/city_backgroud.png").convert_alpha()
    self.background = pygame.transform.smoothscale(self.background, self.display.get_size())

    def pixel_font(self, size):
        return pixel_font(self, size)

def menu(self):
    while True:
        self.display.blit(self.background, (0, 0))
	    def menu(self):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    """if button_play.check_input(mouse_pos_menu):
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("../assets/audio/BGM_game.mp3")
                        pygame.mixer.music.play(-1)
                        run()"""  # Call the run function from game.py to start the game
                    if button_ldr.check_input(mouse_pos_menu):
                        self.show_leaderboard()
                    if button_credits.check_input(mouse_pos_menu):
