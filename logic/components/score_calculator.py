import time

import health


class ScoreCalculator:


    def score_calculator(self, func):

        score = self.level_timer(self, func) * health
        print(score)
        return score

    #
    # if __name__ == "__main__":
    #     level_timer()
    #     score_calculator()