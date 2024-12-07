import sys, pygame
# from logic.score_db_connection.score_connection_to_saving_score_file import timer, health, score
from user_interface.screens.game import GameLoop
from user_interface.menu_runner import MenuRunner
from user_interface.screens.credits import Credits
from user_interface.screens.end_screen import EndScreen
import user_interface.game_config as config
from user_interface.screens.leaderboard import Leaderboard
from logic.components.timer import Timer

class Runner():

    def __init__(self):
        pygame.init()

        self.dis_width = config.WIDTH
        self.dis_height = config.HEIGHT

        self.display = pygame.display.set_mode((self.dis_width, self.dis_height))

        self.current_state = config.GameState.MENU

        self.timer = None
        self.elapsed_time = 0
        self.character = None



    def run(self):
        menu = MenuRunner(self.display, self)
        game = GameLoop(self.display, self)
        credits = Credits(self.display, self)
        end_screen = EndScreen(self.display, self)
        leaderboard = Leaderboard(self.display, self)

        self.character = game.dog

        game_on = True

        while game_on:
            if self.current_state == config.GameState.MENU:
                menu.menu_runner()
            elif self.current_state == config.GameState.GAMEPLAY:
                self.timer = Timer()
                game.game_loop()
                self.elapsed_time = self.timer.update_time()
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

    def get_elapsed_time(self):
        return self.elapsed_time


if __name__ == "__main__":
    runner = Runner()
    runner.run()
    pygame.quit()
    sys.exit()

