import time


class Misc:
    @staticmethod
    def function_timer(func):
        def inner1(*args, **kwargs):
            # storing time before function execution
            time.time()
            response = func(*args, **kwargs)

            # storing time after function execution
            time.time()
            # print("Total time taken in : ", func.__name__, f"{round(end - begin, 8)} secs")
            return response

        return inner1
