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
    param: factor: '''
    #print(_ease_in_out_sine(step*get_increment(steps))*factor)
    return _ease_in_out_sine(step*get_increment(steps))*factor

def get_factor(steps, angle):
    increment = STOP/steps
    i=0
    s_sum=0
    while i < STOP:
        #print(f"Zähler: {i}, {_ease_in_out_sine(i)}")
        s_sum+=_ease_in_out_sine(i)
        i+=increment
    return angle/s_sum

def get_increment(steps):
    return STOP/steps 

# def get_steps(start, stop, d_angle):
#     '''Calculates the necessary steps for the given angle d_angle to make a smooth movement.
#     :param start: 0
#     :param stop: 0
#     :d_angle: The angle the sensor shall move. '''
#     gc.enable()
#     gc.collect()
#     increment = stop/d_angle #This is one way to determine the increment. Others are better.
#     i = start
#     steps = list()
#     sum_steps = 0
#     while i < stop+increment:
#         sum_steps = sum_steps + _ease_in_out_sine(i)
#         #print(f"i: {i}, Ease: {ease_in_out_sine(i)}")
#         
#         i=i+increment
#     #print(sum_steps)
#     i = start
#     while i < stop-increment:
#         #sum_steps = sum_steps+ ease_in_out_sine(i)
#         #print(f"i: {i}, Ease: {ease_in_out_sine(i)}")
#         steps.append(_ease_in_out_sine(i)*d_angle/sum_steps)
#         i=i+increment
#     return deque(steps,len(steps))

def _ease_in_out_quad(t: float) -> float:
        t *= 2
        if t < 1:
            return 0.5 * t * t
        t -= 1
        return -0.5 * (t * (t - 2) - 1)
    
def _ease_in_out_sine(t: float) -> float:
        return round(abs(-0.5 * (math.cos(math.pi * t) - 1)),2)


def main():    
    #print(loop(0,2,15))
    servo = Servo(0,True,1350,8100)
    servo2 = Servo(1,True,1350,8100)
    #angles = get_steps(0,2,90)
    #increment=0.7 #Anything > 0.7 doesn't make any sense.
    i=0
#     s_sum=0
#     d_angle=50 #Grad
#     #print(f"Vorhersage Summe: {increment*100}")
#     while i < 2.0:
#         print(f"Zähler: {i}, {_ease_in_out_sine(i)}")
#         s_sum+=_ease_in_out_sine(i)
#         i+=increment
#     print(f"Summe sinus: {s_sum}")
    sum_angle=0
#     i=0
#     factor=d_angle/s_sum
    angle=50
    steps=10
    factor = get_factor(steps,angle)
    #increment=get_increment(steps)
#     while i <= STOP:
#         sum_angle+=get_step(i,factor)
#         #print(_ease_in_out_sine(i)*d_angle/sum)
#         print(get_step(i,factor))
#         i+=increment
    print(f"Summe Winkel: {sum_angle}")
    for i in range(0,steps):
        sum_angle+=get_step(i,steps,factor)
        print(get_step(i,steps,factor))
    print(f"Summe Winkel: {sum_angle}")
#     while True: 
#         for i in range(0,5):
#             tmp=60 # start angle
#             for a in angles:
#                 tmp = tmp+a
#                 print(tmp)
#                 servo.set_angle(tmp)
#                 servo2.set_angle(tmp)
#                 sleep_ms(2)
#             for a in angles:
#                 tmp = tmp-a
#                 print(tmp)
#                 servo.set_angle(tmp)
#                 servo2.set_angle(tmp)
#                 sleep_ms(2)
#             
#         for i in range(0,5):
#             tmp=60 # start angle
#             for a in range(0,15):
#                 tmp = tmp + a
#                 print(tmp)
#                 servo.set_angle(tmp)
#                 servo2.set_angle(tmp)
#                 sleep_ms(20)
#             for a in range(15,0,-1):
#                 tmp = tmp-a
#                 print(tmp)
#                 servo.set_angle(a)
#                 servo2.set_angle(tmp)
#                 sleep_ms(20)
#                 


    
if __name__ == "__main__":
    # execute only if run as a script
    main()

