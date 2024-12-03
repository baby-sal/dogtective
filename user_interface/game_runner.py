# from menu import
import sys, pygame
from game import GameLoop
from menu import menu
from user_interface.menu import DogtectiveMenu


class runner():
    #def run_game
        #menu
        #game
        #decorator
        #loop
        #if teddy: score calc
        #credits

    def run(self):
        menu = DogtectiveMenu()
        menu.menu()
        game = GameLoop()
        game.game_loop()
        pygame.quit()
        sys.exit()

