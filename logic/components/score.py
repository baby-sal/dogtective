
class Score:
    def __init__(self):
        pass

    def calculate_score(self, health, elapsed_time):

        bones = health
        lives_bonus = bones * 1000  # Each life is worth 1000 points
        time_score = elapsed_time * 10  # seconds of gameplay indicate poorer performance,\n might need caviat of if time off life bonus<0 return score as 0
        #time_penalty = time_score #to become a negative later
        total_score = lives_bonus + time_score
        print(total_score)
        return total_score
