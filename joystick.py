from machine import Pin,ADC,Timer
from robotlibrary.config import JS_MIN_DUTY, JS_MAX_DUTY, JS_X_MEDIAN, JS_Y_MEDIAN, DEBOUNCE_WAIT, MIN_SPEED, MAX_SPEED
import utime
from robotlibrary.motor import Motor

from collections import deque
class Joystick:
    def __init__(self, x,y,b):
        self.x = ADC(x)
        self.y = ADC(y)
        self.b = Pin(b,Pin.IN, Pin.PULL_UP)
        self.b.irq(trigger=Pin.IRQ_FALLING, handler=self.button_handler)
        self.pressed = False
        self.last_pressed = 0
        self.timer = Timer()
        self.direction_data = deque([JS_X_MEDIAN,JS_X_MEDIAN,JS_X_MEDIAN,JS_X_MEDIAN,JS_X_MEDIAN],5)
        self.speed_data = deque([JS_Y_MEDIAN,JS_Y_MEDIAN,JS_Y_MEDIAN,JS_Y_MEDIAN,JS_Y_MEDIAN],5)
    def reset(self,t):
        self.pressed = False
    
    def button_handler(self,pin):
        while utime.ticks_diff(utime.ticks_ms(), self.last_pressed) < DEBOUNCE_WAIT: 
            pass
        self.last_pressed = utime.ticks_ms()
        if not self.pressed:
            while utime.ticks_diff(utime.ticks_ms(), self.last_pressed) < DEBOUNCE_WAIT:
                pass
            if pin.value() == 1:
                self.pressed=True 
                print(pin.value(), "Button pressed")
                self.last_pressed = utime.ticks_ms()
                self.timer.init(mode=Timer.ONE_SHOT, period=300, callback=self.reset)
    
    def get_speed(self):
        s = self.y.read_u16()
        self.speed_data.popleft()
        self.speed_data.append(s)
        s = int(sum(self.speed_data)/len(self.speed_data))
        speed = 0
        if s < JS_Y_MEDIAN-300:
            speed = abs(JS_MAX_DUTY-s*2)
        elif s > JS_Y_MEDIAN+300:
            speed = -abs(JS_MAX_DUTY-s*2)    
        else:
            speed = 0
        if speed > -4000 and speed < 4000:
                speed = 0
        return int(MAX_SPEED/JS_MAX_DUTY*speed)
    
    def get_direction(self):
        d = self.x.read_u16()
        self.direction_data.popleft()
        self.direction_data.append(d)
        d = int(sum(self.direction_data)/len(self.direction_data))
        direction = 0
        if d < JS_X_MEDIAN-200:
            direction = -abs(90-(90/JS_X_MEDIAN*d))
        elif d > JS_X_MEDIAN+200:
            direction = abs(90/JS_MAX_DUTY*d)
        else:
            direction = 0
        return int(direction)
    
def main():
    joystick = Joystick(26,27,0)

    while True:
        print(f"X-Werte(Direction): {joystick.get_direction()} | Y-Werte(Speed): {joystick.get_speed()}")
        utime.sleep_ms(1000)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()