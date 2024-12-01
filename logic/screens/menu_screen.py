import pygame
import sys
from logic.components.button import Button
from user_interface.game import run


def menu(self):
    while True:
        self.display.blit(self.background, (0, 0))
        mouse_pos_menu = pygame.mouse.get_pos()

        self.text_blit("Dogtective", 200, "royalblue4", 640, 175)
        self.text_blit("MENU", 100, "royalblue4", 640, 275)
        self.dog_image(640, 600)

        button_play = Button(image=None, pos_x=640, pos_y=350, font=self.pixel_font(75), colour="brown", text_in="play")
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
