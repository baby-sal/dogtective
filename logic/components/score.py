
class Score:

    @staticmethod
    def calculate_score(health, elapsed_time):
        bones = health
        lives_bonus = bones * 1000  # Each life is worth 1000 points
        time_score = max(0, (30 - elapsed_time) * 10)  # time bonus awarded for completing level in under 30 seconds
        total_score = lives_bonus + time_score
        return total_score
