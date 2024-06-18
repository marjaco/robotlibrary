from machine import Pin, PWM
import utime
# Version 1.0
class Motor:
    
    def __init__(self, pinNo):
        self.MAX_SPEED = 58000 # The absolute maximum is: 65535. 
        self.gpio = pinNo
        self.speed=0
        self.forward=True
        self.pwm1=PWM(Pin(pinNo))
        self.pwm1.freq(50000)
        self.pwm1.duty_u16(0)
        self.pwm2=PWM(Pin(pinNo+1))
        self.pwm2.freq(50000)
        self.pwm2.duty_u16(0)
        self.MIN_SPEED = 0
        self.MAX_SPEED = 100

    def set_speed(self,s):
        if s > self.MIN_SPEED and s < self.MAX_SPEED:
            self.pwm1.duty_u16(int(self.MAX_SPEED*s/100))
            self.speed=s
    
    def off(self):
        self.pwm1.duty_u16(0)
    
    def set_forward(self,forward):
        if self.forward==forward:
            return
        self.pwm1.duty_u16(0)
        self.pwm1,self.pwm2=self.pwm2,self.pwm1        
        self.forward=forward
        self.pwm1.duty_u16(int(self.MAX_SPEED*self.speed/100))
        

