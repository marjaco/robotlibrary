from machine import Pin, PWM
from robotlibrary.config import MIN_DUTY, MAX_DUTY, MAX_SPEED, MIN_SPEED
import utime
# Version 1.0
class Motor:
    
    def __init__(self, pinNo):
        self.gpio = pinNo
        self.speed=0
        self.forward=True
        self.pwm1=PWM(Pin(pinNo))
        self.pwm1.freq(50000)
        self.pwm1.duty_u16(0)
        self.pwm2=PWM(Pin(pinNo+1))
        self.pwm2.freq(50000)
        self.pwm2.duty_u16(0)
        

    def set_speed(self,s):
        '''Sets the speed of the motor. Checks for sensible input.'''
        if s < MIN_SPEED:
            s = 0
        elif s > MAX_SPEED:
            s = MAX_SPEED
        self.pwm1.duty_u16(int(MAX_DUTY*s/100))
        self.speed=s
    
    def off(self):
        self.pwm1.duty_u16(0)
        self.speed = 0
    
    def set_forward(self,forward):
        if self.forward==forward:
            return
        self.pwm1.duty_u16(0)
        self.pwm1,self.pwm2=self.pwm2,self.pwm1        
        self.forward=forward
        self.pwm1.duty_u16(int(MAX_DUTY*self.speed/100))
        

