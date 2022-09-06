import time

def timeme(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        rval = function(*args, **kwargs)
        after = time.time()
        print(f"[INFO] {function.__name__} executed in {after-before} seconds")
        return rval
    return wrapper


@timeme
def foo():
    for i in range(1000):
        print("yellow")


foo()