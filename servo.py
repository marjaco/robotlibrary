from machine import Pin, PWM
import utime

class Servo:
    '''This class manages the servo motor that turns the ultrasonic sensor. You need a servo motor installed to get use out of this. 
    Don't use directly or edit.'''
    def __init__(self,pin):
        self.pin=PWM(Pin(pin))
        self.pin.freq(50)
        self.min=1350
        self.max=8100
        self.angle=0
        
    def set_angle(self,a):
        '''If installed, the servor motor will set the angle of the ultrasonic sensor. 90° ist straight ahead.'''
        if a > self.angle:
            for i in range(self._get_duty(self.angle),self._get_duty(a)):
                self.pin.duty_u16(i)

        elif a < self.angle:
            for i in range(self._get_duty(self.angle), self._get_duty(a),-1):
                self.pin.duty_u16(i)
        self.angle = a
        utime.sleep_ms(4)  
        
    def _get_duty(self,angle):
        '''Internal function. Calculates the PWM duty for the given angle.'''
        return round((self.max-self.min)/180*angle+self.min)
    
    
    
