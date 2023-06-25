import time
import sys

def progress(lst):
    start_time = time.time()
    maxVal = max(lst) + 1
    size = 42
    eta = 0
    for i in lst:
        percent = i/maxVal*100
        barPercent = int(i/maxVal*size)
        cTime = time.time() - start_time
        if percent != 0:
            eta = cTime / percent * 100
        sys.stdout.write(f"\rETA: {eta:.2f}s [{percent:3.0f}%] [{('='*barPercent+'>').ljust(size)}] {i}/{maxVal} | elapsed time {cTime:.2f}s")
        yield i
    sys.stdout.write("\n...")
