# Version 1.92
from machine import Pin
from time import sleep
from time import sleep_ms, sleep_us, ticks_us, ticks_ms
from collections import deque

class Ultra:
    '''This class manages the ultrasonic sensor. It returns the distance to an obstacle in cm. '''
    def __init__(self, pinNo):
        self.trigger = Pin(pinNo, Pin.OUT) # to trigger a sound impulse
        self.echo = Pin(pinNo+1, Pin.IN) # records the echo of the trigger pulse      

    def get_dist(self):
        '''This returns the measured distance in cm. (float)'''
        timepassed = 0
        signalon = 0
        signaloff = 0
        self.trigger.low()
        sleep_us(2)
        self.trigger.high()
        sleep_us(5)
        self.trigger.low()
        starttime = ticks_ms()
        while self.echo.value() == 0:
            if ticks_ms() - starttime > 100:
                break
            signaloff = ticks_us()
        while self.echo.value() == 1:
            if ticks_ms() - starttime > 100:
                break
            signalon = ticks_us()
        timepassed = signalon - signaloff
        distance = round((timepassed * 0.0343) / 2, 2)
        # print("The distance from object is ", distance, "cm.") # for debugging purposes uncomment the line.
        sleep_ms(10) # Wait necessary or program halts
        return distance
    
def main():
    us = Ultra(16)
    dist_values = deque([0,0,0,0,0],5)
    while True:
        d = us.get_dist()
        dist_values.append(d)
        d = sum(dist_values)/len(dist_values)
        print(f"Entfernung: {d} cm")
#     while True: 
#         us = Ultra(16)
#         print(f"Entfernung: {us.get_dist()} cm")

if __name__ == "__main__":
    # execute only if run as a script
    main()