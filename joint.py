# peripherals
from robotlibrary.servo_crab import Servo
import robotlibrary.config
from time import sleep, sleep_ms

class Joint:
    FRONT_FORWARD_ANGLE = 160
    FRONT_BACKWARD_ANGLE = 110
    REAR_FORWARD_ANGLE = 90
    REAR_BACKWARD_ANGLE = 40
    UP_ANGLE = 80
    DOWN_ANGLE = 100
    def __init__(self, s_type, name, left_side, inverted, pin):
        self.NAME = name
        self.s_type = s_type
        
        self.__min_duty = robotlibrary.config.SERVO_MIN_DUTY
        self.__max_duty = robotlibrary.config.SERVO_MAX_DUTY
        
        self.left_side = left_side
        
        if s_type == robotlibrary.config.SHOULDER_FRONT:
            self.__min_angle = robotlibrary.config.SHOULDER_FRONT_MIN_ANGLE
            self.__max_angle = robotlibrary.config.SHOULDER_FRONT_MAX_ANGLE
        elif s_type == robotlibrary.config.SHOULDER_REAR:
            self.__min_angle = robotlibrary.config.SHOULDER_REAR_MIN_ANGLE
            self.__max_angle = robotlibrary.config.SHOULDER_REAR_MAX_ANGLE
        elif s_type == robotlibrary.config.KNEE:
            self.__min_angle = robotlibrary.config.KNEE_MIN_ANGLE
            self.__max_angle = robotlibrary.config.KNEE_MAX_ANGLE
            self.__min_duty = 1800
            self.__max_duty = 7600
        self.servo = Servo(pin, inverted, self.__min_duty, self.__max_duty)
        
        
    @property
    def min_duty(self):
        return self.__min_duty     
       
    @min_duty.setter
    def set_min_duty(value):
        print(value)
        self.__min_duty = value    
        
    @property
    def max_duty(self):
        return self.__max_duty     
       
    @max_duty.setter
    def set_max_duty(value):
        self.__max_duty = value  
          
    @property
    def min_angle(self):
        return self.__min_angle

    @min_angle.setter
    def set_min_angle(a):
        self.__min_angle = a

    @property
    def max_angle(self):
        return self.__max_angle

    @max_angle.setter
    def set_max_angle(a):
        self.__max_angle = a
        
#     def up(self) -> bool:
#         if self.s_type == robotlibrary.config.KNEE and self.servo.angle > self.UP_ANGLE:
#             self.servo.set_angle(self.servo.angle -2)
#             return True
#         return False
#     
#     def down(self) -> bool:
#         if self.s_type == robotlibrary.config.KNEE and self.servo.angle < self.DOWN_ANGLE:
#             self.servo.set_angle(self.servo.angle +2)
#             return True
#         return False
    def up(self):
        self.servo.set_angle(self.UP_ANGLE)
        return False
    def down(self):
        self.servo.set_angle(self.DOWN_ANGLE)
        return False
#     def move_up(self):
#         if self.s_type == robotlibrary.config.KNEE:
#             self.servo.set_angle(60)
#             return True
#         return False
#     def move_down(self):
#         if self.s_type == robotlibrary.config.KNEE:
#             self.servo.set_angle(120)
#             return True
#         return False
    def forward(self) -> bool:
        if not self.left_side:
            if self.s_type == robotlibrary.config.SHOULDER_FRONT and self.servo.angle < self.FRONT_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle +2)
                #print(f"Winkel rechts vorne: {self.servo.angle +2}")
                return True
            if self.s_type == robotlibrary.config.SHOULDER_REAR and self.servo.angle < self.REAR_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle +2)
                #print(f"Winkel rechts hinten: {self.servo.angle +2}")
                return True
            return False
        else:
            #print(self.servo.angle)
            if self.s_type == robotlibrary.config.SHOULDER_FRONT and self.servo.angle > 180-self.FRONT_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle - 2)
                #print(f"Winkel links vorne: {self.servo.angle -2}")
                return True
            if self.s_type == robotlibrary.config.SHOULDER_REAR and self.servo.angle > 180-self.REAR_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle - 2)
                #print(f"Winkel links hinten: {self.servo.angle -2}")
                return True
            return False

    def backward(self) -> bool:
        if not self.left_side:
            if self.s_type == robotlibrary.config.SHOULDER_FRONT and self.servo.angle > self.FRONT_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle -2)
                return True
            if self.s_type == robotlibrary.config.SHOULDER_REAR and self.servo.angle > self.REAR_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle -2)
                return True
            return False
        else:
            if self.s_type == robotlibrary.config.SHOULDER_FRONT and self.servo.angle < 180-self.FRONT_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle + 2)
                return True
            if self.s_type == robotlibrary.config.SHOULDER_REAR and self.servo.angle < 180-self.REAR_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle + 2)
                return True
            return False
        

    def park(self):
        if self.s_type == robotlibrary.config.KNEE:
            self.servo.set_angle(self.min_angle)
        elif self.s_type == robotlibrary.config.SHOULDER_FRONT:
            if not self.left_side: 
                self.servo.set_angle(self.max_angle)
            else:
                self.servo.set_angle(180-self.max_angle)
        else:
            if not self.left_side: 
                self.servo.set_angle(self.min_angle)
            else:
                self.servo.set_angle(180-self.min_angle)
    
    def curl(self):
        if self.s_type == robotlibrary.config.KNEE:
            self.servo.set_angle(self.max_angle)
        elif self.s_type == robotlibrary.config.SHOULDER_FRONT or self.s_type == robotlibrary.config.SHOULDER_REAR:
            self.servo.set_angle(90)
                
    def tap(self):
        if self.s_type == robotlibrary.config.KNEE:
            for i in range(3):
                self.servo.set_angle(85)
                sleep_ms(50)
                self.servo.set_angle(70)
                sleep_ms(50)
            
    def calibrate(self):
        self.servo.set_angle(90)
        
    def __set_angle(self,a):
        if not self.left_side:
            self.servo.set_angle(a)
            print(f"Winkel rechts: {a}")
        else:
            self.servo.set_angle(180-a)
            print(f"Winkel links: {a}")
        
def main():    
    j = Joint(robotlibrary.config.KNEE, "rear left", True, True, 1)
    print(j.__min_angle, j.__max_angle)
    j.curl()
    print(j.__dict__)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()