import pygame
from logic.screens.credits import credit_screen
from logic.screens.leaderboard import leaderboard
from logic.screens.menu_screen import menu
from logic.screens.menu_display import dog_image, pixel_font, text_blit, credit_blit
from user_interface.game_config import WIDTH, HEIGHT

class DogtectiveMenu:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Dogtective: Main Menu")
        self.background = pygame.image.load("../logic/assets/images/menu/city_backgroud.png").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background, self.display.get_size())
        pygame.mixer.music.load("../logic/assets/audio/BGM_menu.mp3")
        pygame.mixer.music.play(-1)

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
