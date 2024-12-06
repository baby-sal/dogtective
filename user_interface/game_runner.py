# from menu import
import sys, pygame

from logic.score_db_connection.score_connection_to_saving_score_file import score
from user_interface.screens.game import GameLoop
from user_interface.menu_runner import MenuRunner
from user_interface.screens.credits import Credits
from user_interface.screens.end_screen import EndScreen
import user_interface.game_config as config
from user_interface.screens.leaderboard import Leaderboard
# from logic.components.timer import Timer
from logic.components.score_calculator import ScoreCalculator

class Runner():

    #while window == open:
        #def run_game:
            #while state = menu:
                #menu
            #if state = game
            #decorator
            #loop
             #if teddy: return time
                #score calc
            #credits

    def __init__(self):
        pygame.init()

        self.dis_width = config.WIDTH
        self.dis_height = config.HEIGHT

        self.display = pygame.display.set_mode((self.dis_width, self.dis_height))

        self.current_state = config.GameState.MENU

    # def level_time(self):
    #     level_time = Timer

    def run(self):
        menu = MenuRunner(self.display, self)
        game = GameLoop(self.display, self)
        credits = Credits(self.display, self)
        end_screen = EndScreen(self.display, self)
        leaderboard = Leaderboard(self.display)

        game_on = True

        while game_on:
            if self.current_state == config.GameState.MENU:
                menu.menu_runner()
            elif self.current_state == config.GameState.GAMEPLAY:
                time = game.game_loop()
                print(time)
                #ScoreCalculator() #in the score calculator class import from character or something the health and the time
            elif self.current_state == config.GameState.CREDITS:
                credits.credit_screen()
            elif self.current_state == config.GameState.LEADERBOARD:
                leaderboard.show()
            elif self.current_state == config.GameState.WIN:
                end_screen.you_win()
            elif self.current_state == config.GameState.LOSE:
                end_screen.you_lose()
            else:
                game_on = False


if __name__ == "__main__":
    runner = Runner()
    runner.run()
    pygame.quit()
    sys.exit()

