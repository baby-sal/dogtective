# from menu import
import sys, pygame
from user_interface.screens.game import GameLoop
from user_interface.menu_runner import MenuRunner
import user_interface.game_config as config


class Runner():

    state = "MENU"

    #def run_game
        #menu
        #game
        #decorator
        #loop
        #if teddy: score calc
        #credits

    def __init__(self):
        pygame.init()

        self.dis_width = config.WIDTH
        self.dis_height = config.HEIGHT

        self.display = pygame.display.set_mode((self.dis_width, self.dis_height))


    def run(self):
        menu = MenuRunner(self.display)
        menu.menu_runner()
        game = GameLoop(self.display)
        game.game_loop()
        pygame.quit()
        sys.exit()

        # if state == "MENU":
        #   menu.menu_runner()
        # elif state == "GAMEPLAY":
        #   game.game_loop()
        # elif state == "CREDITS":
        #   credits.cresits()

