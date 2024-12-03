import time
#make this a decorator?
#constants

class Timer:

    allowed_time = 600

    def timer_start():
         #10 minutes
        time_start = time.time()
        time.sleep(1)
        return time_start

    def timer_end(time_start, allowed_time):
            time_elapsed = allowed_time - time_start


    def screen_timer():
        pass

    timer_start()
    print("time passes")
    timer_end()