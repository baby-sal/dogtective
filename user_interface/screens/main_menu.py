import pygame
from credits import credit_screen
from leaderboard import leaderboard
from menu_display import pixel_font, text_blit,  background_image
import user_interface.game_config as config

class DogtectiveMenu:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("Dogtective: Main Menu")
        self.load_background_image()

    def load_background_image(self):
        background_image(self)

    def pixel_font(self, size):
        return pixel_font(self, size)

    def text_blit(self, text, size, colour, rect_pos_x, rect_pos_y):
        text_blit(self, text, size, colour, rect_pos_x, rect_pos_y)

    def show_credits(self):
        credit_screen(self)

    def show_leaderboard(self):
        leaderboard(self)

if __name__ == "__main__":
    menu_instance = DogtectiveMenu()
    menu_instance.show_menu()