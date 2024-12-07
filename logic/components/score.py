import pygame  # Import the Pygame library

# class Timer:
#     def __init__(self):
#         # Initialize the Timer class and record the start time
#         self.start_ticks = pygame.time.get_ticks()
#
#     def update(self):
#         # Calculate the elapsed time in seconds since the start time
#         elapsed_seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
#         return elapsed_seconds


class Score:
    def __init__(self, timer, character):
        # Initialize the Score class with references to the Timer and Character instances
        self.timer = timer
        self.character = character
        self.points = 0

    def calculate_score(self, health, play_time):

        lives_bonus = health * 1000  # Each life is worth 1000 points
        time_score = play_time * 10  # seconds of gameplay indicate poorer performance,\n might need caviat of if time off life bonus<0 return score as 0
        #time_penalty = time_score #to become a negative later
        total_score = lives_bonus + time_score
        print(total_score)
        return total_score
