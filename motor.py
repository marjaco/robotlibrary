# Version 1.90
from machine import Pin, PWM
from robotlibrary.config import MIN_DUTY, MAX_DUTY, MAX_SPEED, MIN_SPEED
import math
from time import sleep, sleep_ms

class Motor:
    '''This class manages the motor. Don't edit!'''
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
        self.speed_offset = 0

    def set_speed(self,s):
        '''Sets the speed of the motor. Checks for sensible input.'''
        if s + self.speed_offset <= MIN_SPEED:
            s = 0
            self.reset_offset()
        elif s + self.speed_offset >= MAX_SPEED:
            s = MAX_SPEED
            self.reset_offset()
        self.pwm1.duty_u16(int(math.floor((MAX_DUTY*(s+self.speed_offset)/MAX_SPEED)+(MIN_DUTY/MAX_SPEED*(MAX_SPEED-(s+self.speed_offset))))))
        self.speed=s
    
    def change_speed(self,sc):
        '''This defines an offset to the speed in motor. It is used with the remote control to turn the robot.'''
        if self.speed + sc > MIN_SPEED and self.speed + sc < MAX_SPEED: 
            self.speed_offset += sc
            self.set_speed(self.speed)
        
    def reset_offset(self):
        self.speed_offset = 0
        
    def off(self):
        self.pwm1.duty_u16(0)
        self.speed = 0
    
    def set_forward(self,forward):
        '''Sets the motor to forward or backward without changing the speed. '''
        if self.forward==forward:
            return
        self.pwm1.duty_u16(0)
        self.pwm1,self.pwm2=self.pwm2,self.pwm1        
        self.forward=forward
        self.set_speed(self.speed)
        
def main():
    try:
        motor = Motor(14)
        for i in range(MIN_SPEED,MAX_SPEED+1,5):
            print(int(math.floor((MAX_DUTY*(i)/MAX_SPEED)+(MIN_DUTY/MAX_SPEED*(MAX_SPEED-(i))))))
            motor.set_speed(i)
            sleep_ms(100)
        motor.off()
    except KeyboardInterrupt:
        print("Program interrupted.")
        motor.off()
        
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
