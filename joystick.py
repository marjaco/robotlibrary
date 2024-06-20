from machine import Pin,ADC
import utime
from robotlibrary.motor import Motor
class Joystick:
    def __init__(self, x,y,b):
        self.x = ADC(x)
        self.y = ADC(y)
        self.b = Pin(b,Pin.IN, Pin.PULL_UP)
        self.b.irq(trigger=Pin.IRQ_FALLING, handler=self.button_handler)
    
    def button_handler(self,pin):
        pass
    
    def get_speed(self,s):
        speed = 0
        if s < 29600:
            speed = abs(Motor.MAX_DUTY-s*2)
        elif s > 30500:
            speed = -abs(Motor.MAX_DUTY-s*2)    
        else:
            speed = 0
        if speed > -4000 and speed < 4000:
                speed = 0
        return int(100/Motor.MAX_DUTY*speed)
    
    
    def get_direction(self,d):
        if s < 29600:
            return abs(65535-s*2)
        elif s > 30500:
            return -abs(65535-s*2)
        else:
            return 0

joystick = Joystick(26,27,0)

while True:
    #print(f"X-Werte: {joystick.x.read_u16()}")
    print(f"Y-Werte: {joystick.get_speed(joystick.y.read_u16())}")
    utime.sleep_ms(1000)