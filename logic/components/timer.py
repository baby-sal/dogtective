import time

import pygame.time


# from logic.components.score import timer


class Timer:
    #decorator, ns
# def level_timer(func):
#     def inner_timer(*args, **kwargs):
#         time_start = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         time_elapsed = end_time - time_start
#         return time_elapsed
#     return inner_timer

    def __init__(self):
        self.start_ticks = pygame.time.get_ticks()

        def update_time(self):
            elapsed_second = (pygame.time.get_ticks() - self.start_ticks) // 1000
            return elapsed_second