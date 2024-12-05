import time

from logic.components.score import timer


class Timer:
    def timer(self, func):
        def inner_timer(*args, **kwargs):
            time_start = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            time_elapsed = end_time - time_start
            print(time_elapsed)
            return value
        return inner_timer


    @timer
    def addx(num):
        return num+1


    print(addx(1))