# Version 2.0.1
import math
from robotlibrary.servo import Servo
from time import sleep_ms
from collections import deque
import gc
START=0
STOP=2

def get_step(step,steps,factor):
    '''param: step: step number
    param: steps: number of steps for the whole movement
    param: factor: the factor to multiply the step with'''
    return _ease_in_out_sine(step*_get_increment(steps))*factor

def get_factor(steps, angle):
    increment = STOP/steps
    i=0
    s_sum=0
    while i < STOP:
        #print(f"Zähler: {i}, {_ease_in_out_sine(i)}")
        s_sum+=_ease_in_out_sine(i)
        i+=increment
    return angle/s_sum

def _get_increment(steps):
    return STOP/steps 

def _ease_in_out_quad(t: float) -> float:
        t *= 2
        if t < 1:
            return 0.5 * t * t
        t -= 1
        return -0.5 * (t * (t - 2) - 1)
    
def _ease_in_out_sine(t: float) -> float:
        return abs(-0.5 * (math.cos(math.pi * t) - 1))


def main():    
    pass

if __name__ == "__main__":
    # execute only if run as a script
    main()

