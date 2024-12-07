
class NegativeTime(Exception):
    pass

class ZeroOrNegativeLives(Exception):
    pass

class Score:

    @staticmethod
    def calculate_score(health, elapsed_time):
        bones = health
        lives_bonus = bones * 1000  # Each life is worth 1000 points
        time_score = max(0, (30 - elapsed_time) * 10)  # time bonus awarded for completing level in under 30 seconds
        total_score = lives_bonus + time_score

        #score exception handling
        if elapsed_time < 0:
            raise NegativeTime("No negative time")
        if bones < 1:
            raise ZeroOrNegativeLives("Health may not be less that one when calculating score as one is the minimum to complete the level")

        return total_score


