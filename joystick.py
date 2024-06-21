from machine import Pin,ADC,Timer
import utime
from robotlibrary.motor import Motor
X_MEDIAN = 29940
Y_MEDIAN = 30510
MAX_DUTY = 65535
MIN_DUTY = 260
DEBOUNCE_WAIT = 100
class Joystick:
    def __init__(self, x,y,b):
        self.x = ADC(x)
        self.y = ADC(y)
        self.b = Pin(b,Pin.IN, Pin.PULL_UP)
        self.b.irq(trigger=Pin.IRQ_FALLING, handler=self.button_handler)
        self.pressed = False
        self.last_pressed = 0
        self.timer = Timer()
        
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
    
    def get_speed(self,s):
        speed = 0
        if s < Y_MEDIAN-300:
            speed = abs(MAX_DUTY-s*2)
        elif s > Y_MEDIAN+300:
            speed = -abs(MAX_DUTY-s*2)    
        else:
            speed = 0
        if speed > -4000 and speed < 4000:
                speed = 0
        return int(100/MAX_DUTY*speed)
    
    def get_direction(self,d):
        direction = 0
        if d < X_MEDIAN-200:
            direction = -abs(90-(90/X_MEDIAN*d))
        elif d > X_MEDIAN+200:
            direction = abs(90/65535*d)
        else:
            direction = 0
        return int(direction)

joystick = Joystick(26,27,0)

while True:
#     y_values = list()
#     x_values = list()
#     for i in range(0,100):
#         x_values.append(joystick.x.read_u16())
#         y_values.append(joystick.y.read_u16())
#     sum = 0
#     print(y_values)
#     for y in y_values:
#         sum += y
    #print(f"Yvalues median: {sum/100}")
    #print(f"X-Werte: {joystick.x.read_u16()}")
    #print(f"Y-Werte: {joystick.y.read_u16()}")

    print(f"X-Werte: {joystick.get_direction(joystick.x.read_u16())}")
    print(f"Y-Werte: {joystick.get_speed(joystick.y.read_u16())}")
    utime.sleep_ms(1000)