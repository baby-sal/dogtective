import pygame
import sys
from pygame.examples.cursors import image
from logic.components.button import Button
from game import run
import user_interface.game_config as config

class DogtectiveMenu:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("Dogtective: Main Menu")
        self.background = pygame.image.load("../logic/assets/images/menu/city_backgroud.png").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background, self.display.get_size())

    def pixel_font(self, size):
        return pygame.font.Font("../logic/assets/StayPixelRegular.ttf", size)

    def text_blit(self, text, size, colour, rect_pos_x, rect_pos_y):
        text = self.pixel_font(size).render(text, True, colour)
        rect = text.get_rect(center=(rect_pos_x, rect_pos_y))
        self.display.blit(text, rect)

    def credit_blit(self, text, pos_y):
        text = self.pixel_font(40).render(text, True, "crimson")
        rect = text.get_rect(center=(640, pos_y))
        self.display.blit(text, rect)

    def dog_image(self, pos_x, pos_y):
        smol_dog_pic = pygame.image.load("../logic/assets/images/characters/dogtective_sprite/Walk.png").convert_alpha()
        rect_dog = smol_dog_pic.get_rect(center=(pos_x, pos_y))
        self.display.blit(smol_dog_pic, rect_dog)

    def leaderboard(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if go_back.check_input(mouse_pos_ldr):
                    #     self.menu()
                    pass
            pygame.display.update()

    def credit_screen(self):
        while True:
            pygame.display.set_caption("Dogtective: Credits")
            mouse_pos_credits = pygame.mouse.get_pos()

            self.display.fill("pink")
            bg = pygame.transform.smoothscale(pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(), self.display.get_size())
            self.display.blit(bg, (0, 0))

            self.text_blit("CREDITS:", 100, "orange", 640, 150)
            self.dog_image(640, 175)
            self.credit_blit("Abbeygayle Potts - co-Project Lead & architect", 250)
            self.credit_blit("Estelle Walford - UI/UX", 300)
            self.credit_blit("Iman Abdelgani - UI/UX & Documentation Lead", 350)
            self.credit_blit("Mel Clarke - Testing", 400)
            self.credit_blit("Sally Davies - UI/UX", 450)
            self.credit_blit("Zarrin Rahman - co-Project Lead & architect", 500)
            self.text_blit("with special thanks to:\nAhmed Abdi - Sound Engineering & Design", 30, "darkblue", 640, 600)

            button_go_back = Button(image=None, pos_x=1200, pos_y=50, font=self.pixel_font(40), colour="purple4", text_in="go back")
            button_go_back.update_button(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_go_back.check_input(mouse_pos_credits):
                        self.menu()

            pygame.display.update()

    def menu(self):
        while True:
            self.display.blit(self.background, (0, 0))
            mouse_pos_menu = pygame.mouse.get_pos()

            self.text_blit("Dogtective", 200, "royalblue4", 640, 175)
            self.text_blit("MENU", 100, "royalblue4", 640, 275)
            self.dog_image(640, 600)

            button_play = Button(image=None, pos_x=640, pos_y=350, font=self.pixel_font(75), colour="brown", text_in="play")
            button_ldr = Button(image=None, pos_x=640, pos_y=425, font=self.pixel_font(75), colour="lightsalmon", text_in="LEADERBOARD")
            button_credits = Button(image=None, pos_x=640, pos_y=500, font=self.pixel_font(75), colour="lightsalmon", text_in="CREDITS")

            for button in [button_play, button_ldr, button_credits]:
                button.update_button(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_play.check_input(mouse_pos_menu):
                        run()
                    # if button_ldr.check_input(mouse_pos_menu):
                    #     self.leaderboard()
                    if button_credits.check_input(mouse_pos_menu):
                        self.credit_screen()
            pygame.display.update()


if __name__ == "__main__":
    menu = DogtectiveMenu()
    menu.menu()
