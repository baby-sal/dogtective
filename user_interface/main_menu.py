import pygame
import os
from logic.screens.credits import credit_screen
from logic.screens.leaderboard import leaderboard
from logic.screens.menu_screen import menu
from logic.screens.menu_display import dog_image, pixel_font, text_blit, credit_blit
import user_interface.game_config as config

class DogtectiveMenu:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("Dogtective: Main Menu")
        self.background_image = self.load_background_image()
        self.background_image = pygame.transform.smoothscale(self.background_image, self.display.get_size())
        self.display.blit(self.background_image, (0, 0))

    def load_background_image(self):
        print("Current working directory:", os.getcwd())

        # Correctly form the path
        image_path = os.path.normpath(os.path.join(os.getcwd(), "../logic/assets/images/menu/city_background.png"))
        print("Loading image from path:", image_path)

        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"The file {image_path} was not found.")

        background_image = pygame.image.load(image_path).convert_alpha()
        return background_image

    def pixel_font(self, size):
        return pixel_font(self, size)

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
