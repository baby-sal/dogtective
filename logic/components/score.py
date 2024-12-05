import pygame  # Import the Pygame library
from logic.score_db_connection.db_utils_score import DbClass

class Health:
    def __init__(self, max_health):
        # Initialize the Health class with maximum health value
        self.max_health = max_health
        self.current = max_health

    def decrease_health(self, amount):
        # Decrease the current health by a given amount, ensuring it doesn't drop below zero
        self.current -= amount
        if self.current < 0:
            self.current = 0

    def increase_health(self, amount):
        # Increase the current health by a given amount, ensuring it doesn't exceed the maximum health
        self.current += amount
        if self.current > self.max_health:
            self.current = self.max_health

class Character:
    def __init__(self, name, health):
        # Initialize the Character class with a name and a Health instance
        self.name = name
        self.health = health


def game_on(timer, character, score):
    # Refresh the display and update the score
    pygame.display.flip()
    return score.update_score()


class Timer:
    def __init__(self):
        # Initialize the Timer class and record the start time
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        # Calculate the elapsed time in seconds since the start time
        elapsed_seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        return elapsed_seconds


class Score:
    def __init__(self, timer, character):
        # Initialize the Score class with references to the Timer and Character instances
        self.timer = timer
        self.character = character
        self.points = 0
        self.db = DbClass()

timer = Timer()
character = Character(name="Dogtective", health=Health(max_health=5))
score = Score(timer, character)