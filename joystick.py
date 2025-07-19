# Version 1.92
from machine import Pin,ADC,Timer
from robotlibrary import config as conf
from time import sleep, sleep_ms,ticks_diff, ticks_ms

from robotlibrary.motor import Motor
from collections import deque

class Joystick:
    def __init__(self, x,y,b):
        self.x = ADC(x)
        self.y = ADC(y)
        self.b = Pin(b,Pin.IN, Pin.PULL_UP)
        self.b.irq(trigger=Pin.IRQ_RISING, handler=self.button_handler)
        self.pressed = False
        self.last_pressed = 0
        self.timer = Timer()
        self.direction_data = deque([conf.JS_X_MEDIAN,conf.JS_X_MEDIAN,conf.JS_X_MEDIAN,conf.JS_X_MEDIAN,conf.JS_X_MEDIAN],5)
        self.speed_data = deque([conf.JS_Y_MEDIAN,conf.JS_Y_MEDIAN,conf.JS_Y_MEDIAN,conf.JS_Y_MEDIAN,conf.JS_Y_MEDIAN],5)
        
    def get_button_pressed(self):
        return self.pressed
    
    def reset(self,t):
        self.pressed = False
    
    def button_handler(self,pin):
        while ticks_diff(ticks_ms(), self.last_pressed) < conf.DEBOUNCE_WAIT: 
            pass
        self.last_pressed = ticks_ms()
        if not self.pressed:
            while ticks_diff(ticks_ms(), self.last_pressed) < conf.DEBOUNCE_WAIT:
                pass
            if pin.value() == 1:
                self.pressed=True 
                print(pin.value(), "Button pressed")
                self.last_pressed = ticks_ms()
                self.timer.init(mode=Timer.ONE_SHOT, period=300, callback=self.reset)
    
    def get_speed(self):
        s = self.y.read_u16()
        self.speed_data.append(s)
        s = int(sum(self.speed_data)/len(self.speed_data))
        speed = 0
        if s < conf.JS_Y_MEDIAN-300:
            speed = abs(conf.JS_MAX_DUTY-s*2)
        elif s > conf.JS_Y_MEDIAN+300:
            speed = -abs(conf.JS_MAX_DUTY-s*2)    
        else:
            speed = 0
        if speed > -1000 and speed < 1000:
                speed = 0
        return int(conf.MAX_SPEED/conf.JS_MAX_DUTY*speed)
    
    def get_direction(self):
        d = self.x.read_u16()
        self.direction_data.append(d)
        d = int(sum(self.direction_data)/len(self.direction_data))
        direction = 0
        if d < conf.JS_X_MEDIAN-200:
            #direction = - abs(90-(90/conf.JS_MAX_DUTY * d))
            direction = abs(conf.JS_MAX_DUTY-d*2)
        elif d > conf.JS_X_MEDIAN+200:
            #direction = abs(90/conf.JS_MAX_DUTY * d)
            direction = abs(conf.JS_MAX_DUTY-d*2)
        else:
            direction = 0
        return int(90/conf.JS_MAX_DUTY*direction)

    def calibration(self):
        print("calibrating, don't move the joystick.", end='')
        x = [conf.JS_X_MEDIAN for a in range(1000)]
        y = [conf.JS_Y_MEDIAN for b in range(1000)]
        for i in range(0,len(x)):
            print(".", end="")
            x[i] = self.x.read_u16()
            y[i] = self.y.read_u16()
            sleep_ms(2)
        print(" ")
        dx = int(sum(x)/len(x))
        dy = int(sum(y)/len(y))
        print(f"JS_X_MEDIAN value (direction): {dx}")
        print(f"JS_Y_MEDIAN value (speed): {dy}")
        print("Use those values in config.py.")

def main():
    joystick = Joystick(26,27,0)
    while True: 
        print(joystick.x.read_u16())
        sleep_ms(100)
    #joystick.calibration()
#     while True:
#         print(f"Speed: {joystick.get_speed()}, Direction: {joystick.get_direction()}")
#         sleep_ms(50)

if __name__ == "__main__":
    # execute only if run as a script
    main()
