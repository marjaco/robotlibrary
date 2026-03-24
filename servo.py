# Version 2.0.2

from machine import Pin, PWM
from time import sleep_ms, sleep_us

from robotlibrary import config as conf
class Servo:
    '''This class manages the servo motor that turns the ultrasonic sensor. You need a servo motor installed to get use out of this. 
    Don't use directly or edit if you don't know what you are doing.'''
    
    def __init__(self,pin,inverted, min_duty, max_duty):
        self.inverted = inverted
        self.pin=PWM(Pin(pin))
        self.pin.freq(50)
        self.min=min_duty
        self.max=max_duty
        self.set_angle(90)
        self.__wait=150
        
    @property
    def angle(self):
        return self.__angle
    
    def calibrate(self):
        self.pin.duty_u16(self.__get_duty(90))
        
    def set_angle(self,a):
        '''This sets the angle of the servo motor immediately. '''
        if 0 <= a <= 180:
            self.__angle = a
            if not self.inverted: 
                self.pin.duty_u16(self.__get_duty(self.__angle))
            else:
                self.pin.duty_u16(self.__get_duty(180-self.__angle))
            sleep_ms(5)
     
    def set_angle_slowly(self,a):
        ''' This sets the angle of the servo motor slowly.'''
        if a > self.__angle:
            if not self.inverted:
                for i in range(self.__get_duty(self.__angle),self.__get_duty(a)):
                    self.pin.duty_u16(i)
                    sleep_us(self.__wait)
            else: 
                for i in range(self.__get_duty(180-self.__angle),self.__get_duty(a), -1):
                    self.pin.duty_u16(i)
                    sleep_us(self.__wait)
        elif a < self.__angle:
            if not self.inverted:
                for i in range(self.__get_duty(self.__angle), self.__get_duty(a),-1):
                    self.pin.duty_u16(i)
                    sleep_us(self.__wait)
            else: 
                for i in range(self.__get_duty(180-self.__angle), self.__get_duty(a)):
                    self.pin.duty_u16(i)
                    sleep_us(self.__wait)
        self.__angle = a
        #sleep_ms(8)
        
    def __get_duty(self,angle):
        '''Internal function. Calculates the PWM duty for the given angle.'''
        return round((self.max-self.min)/180*angle+self.min)
    
def main():
    s = Servo(0, False, conf.SERVO_MIN_DUTY, conf.SERVO_MAX_DUTY)
    s.set_angle(0)
    for i in range(10):
        print(f"Turn {i}")
        s.set_angle(0)
        sleep_ms(500)
        s.set_angle(180)
        sleep_ms(500)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
    

