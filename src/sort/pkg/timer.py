import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_taken_ms = (end - start) * 1000
        print(f"Time taken: {time_taken_ms} (ms)")
        return result

    return wrapper
