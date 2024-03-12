import time
import sys

def rotate_animation():
    chars = ['-', '\\', '|', '/']
    delay = 0.1

    while True:
        for char in chars:
            sys.stdout.write('\r' + char)
            sys.stdout.flush()
            time.sleep(delay)

if __name__ == "__main__":
    rotate_animation()
