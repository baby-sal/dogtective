from threading import Timer

import pygame  # Import the Pygame library
from logic.components.character import Character
from logic.score_db_connection.score_connection_to_saving_score_file import health

health = Character("dog", health)
timer = Timer


def game_on(timer, score):
    # Refresh the display and update the score
    pygame.display.flip()
    return score.update_score()

def Score(health, play_time):
    lives_bonus = health * 1000  # Each life is worth 1000 points
    time_bonus = play_time * 10  # Each second is worth 10 points
    total_score = lives_bonus + time_bonus
    return total_score

class Timer:
    def __init__(self):
        # Initialize the Timer class and record the start time
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        # Calculate the elapsed time in seconds since the start time
        elapsed_seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000#shows the time elapsed in seconds
        return elapsed_seconds



