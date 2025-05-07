from machine import Pin, PWM
import time
import robotlibrary.config

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
    @property
    def angle(self):
        return self.__angle
    
    def calibrate(self):
        self.pin.duty_u16(self.__get_duty(90))
        
    def set_angle(self,a):
        #print(f"Setting angle: {a}")
        if 0 <= a <= 180:
            self.__angle = a
            if not self.inverted: 
                self.pin.duty_u16(self.__get_duty(self.__angle))
            else:
                self.pin.duty_u16(self.__get_duty(180-self.__angle))
            time.sleep_ms(5)
     
    def set_angle_slowly(self,a):
        '''If installed, the servor motor will set the angle of the ultrasonic sensor. 90° ist straight ahead.'''
        if a > self.__angle:
            if not self.inverted:
                for i in range(self.__get_duty(self.__angle),self.__get_duty(a)):
                    self.pin.duty_u16(i)
            else: 
                for i in range(self.__get_duty(180-self.__angle),self.__get_duty(a), -1):
                    self.pin.duty_u16(i)
        elif a < self.__angle:
            if not self.inverted:
                for i in range(self.__get_duty(self.__angle), self.__get_duty(a),-1):
                    self.pin.duty_u16(i)
            else: 
                for i in range(self.__get_duty(180-self.__angle), self.__get_duty(a)):
                    self.pin.duty_u16(i) 
        self.__angle = a
        time.sleep_ms(4)
        
    def __get_duty(self,angle):
        '''Internal function. Calculates the PWM duty for the given angle.'''
        return round((self.max-self.min)/180*angle+self.min)
    
def main():
    s = Servo(6, False)
    s.set_angle(120)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
    

