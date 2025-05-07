import math
from robotlibrary.servo import Servo
from time import sleep_ms
def loop(start, stop, angle):
    increment = 2/angle
    i= start
    values = list()
    sum = 0
    while i < stop-increment:
        sum = sum+ ease_in_out_sine(i)
        #print(f"i: {i}, Ease: {ease_in_out_sine(i)}")
        i=i+increment
    #print(sum)
    i=start
    while i < stop-increment:
        #sum = sum+ ease_in_out_quad(i)
        #print(f"i: {i}, Ease: {ease_in_out_sine(i)}")
        values.append(ease_in_out_sine(i)*angle/sum)
        i=i+increment
    sumf = 0.00
    for v in values:
        #print(v)
        sumf = sumf+v
    
    
    #print(sumf)
    #print(sum(values))
    return values
    

def ease_in_out_quad(t: float) -> float:
        t *= 2
        if t < 1:
            return 0.5 * t * t
        t -= 1
        return -0.5 * (t * (t - 2) - 1)
    
def ease_in_out_sine(t: float) -> float:
        return -0.5 * (math.cos(math.pi * t) - 1)


#print(loop(0,2,15))
servo = Servo(0,True,1350,8100)
servo2 = Servo(1,True,1350,8100)
angles = loop(0,2,90)

while True: 
    for i in range(0,5):
        tmp=60
        for a in angles:
            tmp = tmp+a
            #print(tmp)
            servo.set_angle(tmp)
            servo2.set_angle(tmp)
            sleep_ms(2)
        for a in angles:
            tmp = tmp-a
            #print(tmp)
            servo.set_angle(tmp)
            servo2.set_angle(tmp)
            sleep_ms(2)
        
    for i in range(0,5):
        tmp=60
        for a in range(0,15):
            tmp = tmp + a
            servo.set_angle(tmp)
            servo2.set_angle(tmp)
            sleep_ms(20)
        for a in range(15,0,-1):
            tmp = tmp-a
            servo.set_angle(a)
            servo2.set_angle(tmp)
            sleep_ms(20)
            
