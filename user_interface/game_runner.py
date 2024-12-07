# from menu import
import sys, pygame
from user_interface.screens.game import GameLoop
from user_interface.menu_runner import MenuRunner
from user_interface.screens.credits import Credits
from user_interface.screens.end_screen import EndScreen
import user_interface.game_config as config
from user_interface.screens.leaderboard import Leaderboard
from logic.components.timer import Timer
from logic.components.score import calculate_score


class Runner():
    def __init__(self):
        pygame.init()

        self.dis_width = config.WIDTH
        self.dis_height = config.HEIGHT

        self.display = pygame.display.set_mode((self.dis_width, self.dis_height))

        self.current_state = config.GameState.MENU

        self.timer = Timer()
        self.elapsed_time = 0
        self.character = None# will be set in game but needs to be set as none for score


    def run(self):
        menu = MenuRunner(self.display, self)
        game = GameLoop(self.display, self)
        credits = Credits(self.display, self)
        end_screen = EndScreen(self.display, self)
        leaderboard = Leaderboard(self.display, self)

        self.character = game.dog #ensure character is accessible

        game_on = True

        while game_on:
            self.elapsed_time = self.timer.update()
            if self.current_state == config.GameState.MENU:
                menu.menu_runner()
            elif self.current_state == config.GameState.GAMEPLAY:
                game.game_loop()
            elif self.current_state == config.GameState.CREDITS:
                credits.credit_screen()
            elif self.current_state == config.GameState.LEADERBOARD:
                leaderboard.show()
            elif self.current_state == config.GameState.WIN:
                health = self.character.health.current #access character health
                score = calculate_score(health, self.elapsed_time)
                end_screen.you_win()
                return score
            elif self.current_state == config.GameState.LOSE:
                end_screen.you_lose()
                health = self.character.health.current #access character health
                score = calculate_score(health, self.elapsed_time)
                return score
            else:
                game_on = False

        def get_elapsed_time(self):
            return self.elapsed_time # method to access elapsed_time


if __name__ == "__main__":
    runner = Runner()
    runner.run()
    pygame.quit()
    sys.exit()

