import pygame

class Timer:
    def __init__(self):
        # Initialize the Timer class and record the start time
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        # Calculate the elapsed time in seconds since the start time
        elapsed_seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000#shows the time elapsed in seconds
        return elapsed_seconds
