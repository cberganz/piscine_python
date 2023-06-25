import time
from random import randint
import os

def log(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        t = time.perf_counter() - t
        with open("machine.log", mode="a+", encoding="utf-8") as file:
            user = os.getenv('USER', "unknown")
            name = func.__name__.replace('_', ' ').title()
            if t > 0.001:
                file.write(f"({user}) Running: {name:18} [ exec-time = {t:.3f} s ]\n")
            else:
                file.write(f"({user}) Running: {name:18} [ exec-time = {t * 1000:.3f} ms ]\n")
            return result
    return wrapper
