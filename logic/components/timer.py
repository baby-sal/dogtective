import time
import pygame.time

class Timer:

    def __init__(self):
        self.start_ticks = pygame.time.get_ticks()

    def update_time(self):
        elapsed_second = (pygame.time.get_ticks() - self.start_ticks) // 1000
        return elapsed_second
