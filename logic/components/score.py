def calculate_score(health, elapsed_time):
    lives_bonus = health * 1000  # Each life is worth 1000 points
    time_bonus = elapsed_time * 10  # Each second is worth 10 points
    total_score = lives_bonus + time_bonus
    return total_score



