"""from logic.components.button import Button
import pygame
import user_interface.game_config as config
import sys
from user_interface.screens.leaderboard import Leaderboard
from user_interface.screens.credits import Credits

class MainMenu:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("Dogtective: Main Menu")
        self.background = pygame.image.load("..logic/assets/images/menu/city_backgroud.png").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background, self.display.get_size())

    def pixel_font(self, size):
        return pygame.font.Font("../logic/assets/StayPixelRegular.ttf", size)

    def dogtective_image(self, pos_x, pos_y):
        dogtective_pic = pygame.image.load("../logic/assets/images/characters/Dogtective_icon_no_background_1.png").convert_alpha()
        rect_dog = dogtective_pic.get_rect(center=(pos_x, pos_y))
        self.display.blit(dogtective_pic, rect_dog)

    def menu(self):
        while True:
            self.display.blit(self.background, (0, 0))
            mouse_pos_menu = pygame.mouse.get_pos()

            button_play = Button(image=None, pos_x=640, pos_y=350, font=self.pixel_font(75), colour="brown",
                                 text_in="play")
            button_ldr = Button(image=None, pos_x=640, pos_y=425, font=self.pixel_font(75), colour="lightsalmon",
                                text_in="LEADERBOARD")
            button_credits = Button(image=None, pos_x=640, pos_y=500, font=self.pixel_font(75), colour="lightsalmon",
                                    text_in="CREDITS")

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
                        run()
                if button_ldr.check_input(mouse_pos_menu):
                    self.show_leaderboard()
                if button_credits.check_input(mouse_pos_menu):
                    self.show_credits()
            pygame.display.update()

    def show_leaderboard(self):
        # Implement leaderboard display logic
        Leaderboard()

    def show_credits(self):
        # Implement credits display logic
        Credits()


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.menu()
"""