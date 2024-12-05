import time

from logic.components.score import timer


# class Timer:
    #decorator, ns
def level_timer(self, func):
    def inner_timer(*args, **kwargs):
        time_start = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        time_elapsed = end_time - time_start
        print(time_elapsed)
        return value
    return inner_timer