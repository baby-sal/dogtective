import time

from logic.components.score import timer


# class Timer:
    #decorator, ns
def level_timer(func):
    def inner_timer(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        time_elapsed = end_time - time_start
        return time_elapsed
    return inner_timer