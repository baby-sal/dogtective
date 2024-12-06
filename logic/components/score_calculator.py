import time

import health
from logic.components.health import Health


class ScoreCalculator:

    def calculate_score(lives, play_time):
        lives =
        lives_bonus = lives * 1000  # Each life is worth 1000 points
        time_penalty = play_time - 10  # seconds of gameplay indicate poorer performance,\n might need caviat of if time off life bonus<0 return score as 0
        total_score = lives_bonus + time_penalty
        return total_score


    #
    # if __name__ == "__main__":
    #     level_timer()
    #     score_calculator()