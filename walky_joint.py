# Version 1.90
# peripherals
from robotlibrary.servo_crab import Servo
import robotlibrary.config_walky
from time import sleep, sleep_ms

class Joint:
    # HIP_FORWARD_ANGLE = 110
    # HIP_BACKWARD_ANGLE = 80
    # KNEE_FORWARD_ANGLE = 180
    # KNEE_BACKWARD_ANGLE = 120
    def __init__(self, j_type, name, left_side, inverted, pin):
        self.NAME = name
        self.j_type = j_type
        self.__min_duty = robotlibrary.config.walky_config.SERVO_MIN_DUTY
        self.__max_duty = robotlibrary.config.walky_config.SERVO_MAX_DUTY
        self.left_side = left_side
        self.__min_angle = robotlibrary.config.walky_config.SHOULDER_FRONT_MIN_ANGLE
        self.__max_angle = robotlibrary.config.walky_config.SHOULDER_FRONT_MAX_ANGLE
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
        
    def up(self):
        if not self.left_side:
            self.servo.set_angle(robotlibrary.config.walky_config.KNEE_BACKWARD_ANGLE)
        else:
            self.servo.set_angle(180-robotlibrary.config.walky_config.KNEE_BACKWARD_ANGLE)
        return False
    def down(self):
        if not self.left_side:
            self.servo.set_angle(robotlibrary.config.walky_config.KNEE_FORWARD_ANGLE)
        else:
            self.servo.set_angle(180-robotlibrary.config.walky_config.KNEE_FORWARD_ANGLE)
        return False

    def forward(self) -> bool:
        if not self.left_side:
            if self.j_type == robotlibrary.config.walky_config.HIP and self.servo.angle < robotlibrary.config.walky_config.HIP_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle +2)
                #print(f"Winkel rechts vorne: {self.servo.angle +2}")
                return True
            
            return False
        else:
            #print(self.servo.angle)
            if self.j_type == robotlibrary.config.walky_config.HIP and self.servo.angle > 180-robotlibrary.config.walky_config.HIP_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle - 2)
                #print(f"Winkel links vorne: {self.servo.angle -2}")
                return True
            
            return False

    def backward(self) -> bool:
        if not self.left_side:
            if self.j_type == robotlibrary.config.walky_config.HIP and self.servo.angle > robotlibrary.config.walky_config.HIP_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle -2)
                return True
            return False
        else:
            if self.j_type == robotlibrary.config.walky_config.HIP and self.servo.angle < 180-robotlibrary.config.walky_config.HIP_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle + 2)
                return True
            return False
        

    def park(self):
        if self.s_type == robotlibrary.config.walky_config.KNEE:
            self.servo.set_angle(self.min_angle)
        elif self.s_type == robotlibrary.config.walky_config.SHOULDER_FRONT:
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
        if self.s_type == robotlibrary.config.walky_config.KNEE:
            self.servo.set_angle(self.max_angle)
        elif self.s_type == robotlibrary.config.walky_config.SHOULDER_FRONT or self.s_type == robotlibrary.config.walky_config.SHOULDER_REAR:
            self.servo.set_angle(90)
                
    def tap(self):
        if self.s_type == robotlibrary.config.walky_config.KNEE:
            for i in range(3):
                self.servo.set_angle(85)
                sleep_ms(50)
                self.servo.set_angle(70)
                sleep_ms(50)
            
    def calibrate(self):
        if self.j_type == robotlibrary.config.walky_config.HIP: 
            self.servo.set_angle(90)
        else:
            if not self.left_side:
                self.servo.set_angle(180)
            else:
                self.servo.set_angle(0)
        
    def __set_angle(self,a):
        if not self.left_side:
            self.servo.set_angle(a)
            print(f"Winkel rechts: {a}")
        else:
            self.servo.set_angle(180-a)
            print(f"Winkel links: {a}")
        
def main():    
    j = Joint(robotlibrary.config.walky_config.KNEE, "rear left", True, False, 1)
    j.calibrate()
    sleep(30)
    print(j.__min_angle, j.__max_angle)
    while j.up():
        pass
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
