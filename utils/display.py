# utils/display.py
import sys, time

print(f"display.py의 __name__ : {__name__}")
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)