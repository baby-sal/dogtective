from logic.components.character import Character
from user_interface.game_runner import Runner


def calculate_score(self):
    dogtective = Character("Dog", 5)
    runner = Runner()  # create runner instance
    runner.run()  # start the game loop
    elapsed_time = runner.get_elapsed_time()
    lives_bonus = dogtective.health * 1000  # Each life is worth 1000 points
    time_bonus = elapsed_time * 10  # Each second is worth 10 points
    total_score = lives_bonus + time_bonus
    return total_score


