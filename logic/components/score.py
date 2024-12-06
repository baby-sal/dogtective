from threading import Timer

import pygame  # Import the Pygame library
from logic.components.character import Character

dogtective = Character("Dog", 5)


def game_on(timer, score):
    # Refresh the display and update the score
    pygame.display.flip()
    return score.update_score()

class Score:
    def calculate_score(self):
        lives_bonus = dogtective.health * 1000  # Each life is worth 1000 points
        time_bonus = Timer() * 10  # Each second is worth 10 points
        total_score = lives_bonus + time_bonus
        return total_score


