import pygame
import user_interface.game_config as config
from credits import credit_screen
from leaderboard import leaderboard
from menu_screen import menu
from menu_display import dog_image, pixel_font, background_image, text_blit, credit_blit


class DogtectiveMenu:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("Dogtective: Main Menu")
        self.background_image()

    def pixel_font(self, size):
        return pixel_font(self, size)

    def background_image(self):
        background_image(self)

    def text_blit(self, text, size, colour, rect_pos_x, rect_pos_y):
        text_blit(self, text, size, colour, rect_pos_x, rect_pos_y)

    def credit_blit(self, text, pos_y):
        credit_blit(self, text, pos_y)

    def dog_image(self, pos_x, pos_y):
        dog_image(self, pos_x, pos_y)

    def show_menu(self):
        menu(self)

    def show_credits(self):
        credit_screen(self)

    def show_leaderboard(self):
        leaderboard(self)


if __name__ == "__main__":
    menu_instance = DogtectiveMenu()
    menu_instance.show_menu()
