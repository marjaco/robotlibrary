import math
from robotlibrary.servo import Servo
from time import sleep_ms
from collections import deque

def get_steps(start, stop, d_angle):
    increment = stop/d_angle
    i = start
    steps = list()
    sum_steps = 0
    while i < stop-increment:
        sum_steps = sum_steps + ease_in_out_sine(i)
        #print(f"i: {i}, Ease: {ease_in_out_sine(i)}")
        i=i+increment
    i = start
    while i < stop-increment:
        #sum_steps = sum_steps+ ease_in_out_quad(i)
        #print(f"i: {i}, Ease: {ease_in_out_sine(i)}")
        steps.append(ease_in_out_sine(i)*d_angle/sum_steps)
        i=i+increment
    return deque(steps,len(steps))

def ease_in_out_quad(t: float) -> float:
        t *= 2
        if t < 1:
            return 0.5 * t * t
        t -= 1
        return -0.5 * (t * (t - 2) - 1)
    
def ease_in_out_sine(t: float) -> float:
        return -0.5 * (math.cos(math.pi * t) - 1)


def main():    
    #print(loop(0,2,15))
    servo = Servo(0,True,1350,8100)
    servo2 = Servo(1,True,1350,8100)
    angles = get_steps(0,2,90)

    while True: 
        for i in range(0,5):
            tmp=60 # start angle
            for a in angles:
                tmp = tmp+a
                print(tmp)
                servo.set_angle(tmp)
                servo2.set_angle(tmp)
                sleep_ms(2)
            for a in angles:
                tmp = tmp-a
                print(tmp)
                servo.set_angle(tmp)
                servo2.set_angle(tmp)
                sleep_ms(2)
            
        for i in range(0,5):
            tmp=60 # start angle
            for a in range(0,15):
                tmp = tmp + a
                print(tmp)
                servo.set_angle(tmp)
                servo2.set_angle(tmp)
                sleep_ms(20)
            for a in range(15,0,-1):
                tmp = tmp-a
                print(tmp)
                servo.set_angle(a)
                servo2.set_angle(tmp)
                sleep_ms(20)
                


    
if __name__ == "__main__":
    # execute only if run as a script
    main()

