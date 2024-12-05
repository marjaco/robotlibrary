from machine import Pin, PWM
import time
import robotlibrary.config 

class Servo:
    '''This class manages the servo motor that turns the ultrasonic sensor. You need a servo motor installed to get use out of this. 
    Don't use directly or edit if you don't know what you are doing.'''
    
    def __init__(self,pin,inverted):
        self.inverted = inverted
        self.pin=PWM(Pin(pin))
        self.pin.freq(50)
        self.min=robotlibrary.config.SERVO_MIN_DUTY
        self.max=robotlibrary.config.SERVO_MAX_DUTY
        self.__angle=90
        self.set_angle(90)
        #self.calibrate()
    @property
    def angle(self):
        return self.__angle
    
    def calibrate(self):
        self.pin.duty_u16(self.__get_duty(90))
        
    
    def set_angle(self,a):
        if 0 < a < 180:
            self.__angle = a
            if not self.inverted: 
                self.pin.duty_u16(self.__get_duty(self.__angle))
            else:
                self.pin.duty_u16(self.__get_duty(180-self.__angle))
            time.sleep_ms(5)
    
        
    def set_angle_slowly(self,a):
        '''If installed, the servor motor will set the angle of the ultrasonic sensor. 90° ist straight ahead.'''
        print("wrong")
#         if a > self.__angle:
#             for i in range(self.__get_duty(self.__angle),self.__get_duty(a)):
#                 self.pin.duty_u16(i)
#                 time.sleep_us(100)
# 
#         elif a < self.__angle:
#             for i in range(self.__get_duty(self.__angle), self.__get_duty(a),-1):
#                 self.pin.duty_u16(i)
#                 time.sleep_us(100)
#         self.__angle = a
#         time.sleep_ms(4)
        return False
        
    def __get_duty(self,angle):
        '''Internal function. Calculates the PWM duty for the given angle.'''
        return round((self.max-self.min)/180*angle+self.min)
    
def main():
    s = Servo(0, False)
    s.set_angle(60)
if __name__ == "__main__":
    # execute only if run as a script
    main()
    

