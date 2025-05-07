# peripherals
from robotlibrary.servo import Servo
import robotlibrary.config_crawly
from time import sleep, sleep_ms

class Joint:
    # FRONT_FORWARD_ANGLE = 130
    # FRONT_BACKWARD_ANGLE = 90
    # REAR_FORWARD_ANGLE = 90
    # REAR_BACKWARD_ANGLE = 50
    # UP_ANGLE = 75
    # DOWN_ANGLE = 90
    def __init__(self, j_type, name, left_side, inverted, pin):
        '''Initialize a joint in the Crawly robot. 
        Explanation of parameters: 
        j_type: Short for joint_type. Can be robotlibrary.config.crawly_config.SHOULDER_FRONT, robotlibrary.config.crawly_config.SHOULDER_REAR, 
            robotlibrary.config.crawly_config.KNEE
        name: The name of the joint. Use something useful like "front_right". 
        left_side: True or False. Servo motors on the left side need to be inverted in the code. 
        inverted: There are servo motors that turn in a different direction than other. In this case, set to True.
        pin: The pin number that controls the servo motor. 
        '''
        self.name = name
        self.j_type = j_type
        min_duty = robotlibrary.config.crawly_config.SERVO_MIN_DUTY
        max_duty = robotlibrary.config.crawly_config.SERVO_MAX_DUTY
        self.left_side = left_side
        if j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT:
            self.__min_angle = robotlibrary.config.crawly_config.SHOULDER_FRONT_MIN_ANGLE
            self.__max_angle = robotlibrary.config.crawly_config.SHOULDER_FRONT_MAX_ANGLE
        elif j_type == robotlibrary.config.crawly_config.SHOULDER_REAR:
            self.__min_angle = robotlibrary.config.crawly_config.SHOULDER_REAR_MIN_ANGLE
            self.__max_angle = robotlibrary.config.crawly_config.SHOULDER_REAR_MAX_ANGLE
        elif j_type == robotlibrary.config.crawly_config.KNEE:
            self.__min_angle = robotlibrary.config.crawly_config.KNEE_MIN_ANGLE
            self.__max_angle = robotlibrary.config.crawly_config.KNEE_MAX_ANGLE
            min_duty = robotlibrary.config.crawly_config.SERVO_MIN_DUTY_TYPE2 # Comment out if the duty cycle is not different from the shoulder servo's duty cycle.
            max_duty = robotlibrary.config.crawly_config.SERVO_MAX_DUTY_TYPE2 # Comment out if the duty cycle is not different from the shoulder servo's duty cycle.
        self.servo = Servo(pin, inverted, min_duty, max_duty)
          
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
        '''If this object is a knee, it is moved up in one go. As the movement is then finished, it 
        returns False. 
        '''
        if self.j_type == robotlibrary.config.crawly_config.KNEE:
            self.servo.set_angle(robotlibrary.config.crawly_config.CRAWLY_UP_ANGLE)
        return False
    def down(self):
        '''If this object is a knee, it is moved down in one go. As the movement is then finished, it 
        returns False. 
        '''
        if self.j_type == robotlibrary.config.crawly_config.KNEE:
            self.servo.set_angle(robotlibrary.config.crawly_config.CRAWLY_DOWN_ANGLE)
        return False

    def forward(self) -> bool:
        '''See the documentation for crawly_leg.py for information.'''
        if not self.left_side:
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT and self.servo.angle < robotlibrary.config.crawly_config.CRAWLY_FRONT_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle +2)
                return True
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_REAR and self.servo.angle < robotlibrary.config.crawly_config.CRAWLY_REAR_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle +2)
                return True
            return False
        else:
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT and self.servo.angle > 180-robotlibrary.config.crawly_config.CRAWLY_FRONT_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle - 2)
                return True
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_REAR and self.servo.angle > 180-robotlibrary.config.crawly_config.CRAWLY_REAR_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle - 2)
                return True
            return False

    def backward(self) -> bool:
        '''See the documentation for crawly_leg.py for information.'''
        if not self.left_side:
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT and self.servo.angle > robotlibrary.config.crawly_config.CRAWLY_FRONT_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle -2)
                return True
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_REAR and self.servo.angle > robotlibrary.config.crawly_config.CRAWLY_REAR_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle -2)
                return True
            return False
        else:
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT and self.servo.angle < 180-robotlibrary.config.crawly_config.CRAWLY_FRONT_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle + 2)
                return True
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_REAR and self.servo.angle < 180-robotlibrary.config.crawly_config.CRAWLY_REAR_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle + 2)
                return True
            return False
        


    def side_walking_up(self):
        '''If this object is a knee, it is moved slowly. As the movement is then finished, it 
        returns False. 
        '''
        if self.j_type == robotlibrary.config.crawly_config.KNEE:
            self.servo.set_angle(robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_UP_ANGLE)
        return False
    
    def side_walking_down(self):
        '''If this object is a knee, it is moved down slowly. As the movement is then finished, it 
        returns False. 
        '''
        if self.j_type == robotlibrary.config.crawly_config.KNEE:
            self.servo.set_angle(robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_DOWN_ANGLE)
        return False


    def ahead(self) -> bool:
        '''See the documentation for crawly_leg.py for information.'''
        if not self.left_side:
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT and self.servo.angle < robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_FRONT_ANGLE:
                self.servo.set_angle(self.servo.angle + 2)
                return True
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_REAR and self.servo.angle > robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_REAR_ANGLE:
                self.servo.set_angle(self.servo.angle - 2)
                return True
            return False
        else:
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT and self.servo.angle > 180-robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_FRONT_ANGLE:
                self.servo.set_angle(self.servo.angle - 2)
                return True
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_REAR and self.servo.angle < 180-robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_REAR_ANGLE:
                self.servo.set_angle(self.servo.angle + 2)
                return True
            return False

    def center(self) -> bool:
        '''See the documentation for crawly_leg.py for information.'''
        if not self.left_side:
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT and self.servo.angle > robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_CENTER_ANGLE:
                self.servo.set_angle(self.servo.angle - 2)
                return True
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_REAR and self.servo.angle < robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_CENTER_ANGLE:
                self.servo.set_angle(self.servo.angle + 2)
                return True
            return False
        else:
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT and self.servo.angle < 180-robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_CENTER_ANGLE:
                self.servo.set_angle(self.servo.angle + 2)
                return True
            if self.j_type == robotlibrary.config.crawly_config.SHOULDER_REAR and self.servo.angle > 180-robotlibrary.config.crawly_config.CRAWLY_SIDE_WALKING_CENTER_ANGLE:
                self.servo.set_angle(self.servo.angle - 2)
                return True
            return False


        

    def park(self):
        if self.j_type == robotlibrary.config.crawly_config.KNEE:
            self.servo.set_angle(self.min_angle)
        elif self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT:
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
        if self.j_type == robotlibrary.config.crawly_config.KNEE:
            self.servo.set_angle(self.max_angle)
        elif self.j_type == robotlibrary.config.crawly_config.SHOULDER_FRONT or self.j_type == robotlibrary.config.crawly_config.SHOULDER_REAR:
            self.servo.set_angle(90)
                
    def tap(self):
        '''If this joint is a knee, it is tapped three times.'''
        if self.j_type == robotlibrary.config.crawly_config.KNEE:
            for i in range(3):
                self.servo.set_angle(85)
                sleep_ms(50)
                self.servo.set_angle(70)
                sleep_ms(50)
            
    def calibrate(self):
        self.servo.set_angle(0)
        sleep_ms(500)
        self.servo.set_angle(90)
        
    def __set_angle(self,a):
        if not self.left_side:
            self.servo.set_angle(a)
            #print(f"Winkel rechts: {a}") # Uncomment for debug messages.
        else:
            self.servo.set_angle(180-a)
            #print(f"Winkel links: {a}") # Uncomment for debug messages.
        
def main():    
    '''Executed, this sets all servos to 90°.'''
    j = Joint(robotlibrary.config.crawly_config.KNEE, "rear left", True, True, 1)
    j.calibrate()
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
