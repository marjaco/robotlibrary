# peripherals
from robotlibrary.servo import Servo
from robotlibrary import config_crawly as conf
from time import sleep, sleep_ms

class Joint:
    def __init__(self, j_type, name, left_side, inverted, pin):
        '''Initialize a joint in the Crawly robot. 
        Explanation of parameters: 
        j_type: Short for joint_type. Can be conf.SHOULDER_FRONT, conf.SHOULDER_REAR,
            conf.KNEE
        name: The name of the joint. Use something useful like "front_right". 
        left_side: True or False. Servo motors on the left side need to be inverted in the code. 
        inverted: There are servo motors that turn in a different direction than other. In this case, set to True.
        pin: The pin number that controls the servo motor. 
        '''
        self.name = name
        self.j_type = j_type
        min_duty = conf.SERVO_MIN_DUTY
        max_duty = conf.SERVO_MAX_DUTY
        self.left_side = left_side
        if j_type == conf.SHOULDER_FRONT:
            self.__min_angle = conf.SHOULDER_FRONT_MIN_ANGLE
            self.__max_angle = conf.SHOULDER_FRONT_MAX_ANGLE
        elif j_type == conf.SHOULDER_REAR:
            self.__min_angle = conf.SHOULDER_REAR_MIN_ANGLE
            self.__max_angle = conf.SHOULDER_REAR_MAX_ANGLE
        elif j_type == conf.KNEE:
            self.__min_angle = conf.KNEE_MIN_ANGLE
            self.__max_angle = conf.KNEE_MAX_ANGLE
            # min_duty = conf.SERVO_MIN_DUTY_TYPE2 # Comment out if the duty cycle is not different from the shoulder servo's duty cycle.
            # max_duty = conf.SERVO_MAX_DUTY_TYPE2 # Comment out if the duty cycle is not different from the shoulder servo's duty cycle.
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
    
    def up_step(self,increment):
        '''Move the lower thigh up by increment until the minimum angle is reached.
        '''
        if self.j_type == conf.KNEE and self.servo.angle > conf.KNEE_MIN_ANGLE:
            self.servo.set_angle(self.servo.angle - increment)
            return True # The lower thigh is within the safe range.
        return False # The limit of movement is reached.
    
    def down_step(self,increment):
        '''Move the lower thigh down by increment until the maximum angle is reached.
        '''
        if self.j_type == conf.KNEE and self.servo.angle < conf.CRAWLY_DOWN_ANGLE:
            self.servo.set_angle(self.servo.angle + increment)
            return True # The lower thigh is within the safe range.
        return False # The limit of movement is reached.
    
    def forward_step(self, increment):
        '''This moves the leg forward by increment.'''
        if not self.left_side:
            if self.j_type == conf.SHOULDER_FRONT and self.servo.angle < conf.CRAWLY_FRONT_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle + increment)
                return True # The shoulder is within the safe range.
            if self.j_type == conf.SHOULDER_REAR and self.servo.angle < conf.CRAWLY_REAR_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle + increment)
                return True # The shoulder is within the safe range.
            return False # The limit of movement is reached. 
        else:
            if self.j_type == conf.SHOULDER_FRONT and self.servo.angle > 180 - conf.CRAWLY_FRONT_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle - increment)
                return True # The shoulder is within the safe range.
            if self.j_type == conf.SHOULDER_REAR and self.servo.angle > 180 - conf.CRAWLY_REAR_FORWARD_ANGLE:
                self.servo.set_angle(self.servo.angle - increment)
                return True # The shoulder is within the safe range.
            return False # The limit of movement is reached. 
        
    def backward_step(self,increment) -> bool:
        '''This moves the leg backward by increment.'''
        if not self.left_side:
            if self.j_type == conf.SHOULDER_FRONT and self.servo.angle > conf.CRAWLY_FRONT_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle - increment)
                return True # The shoulder is within the safe range. 
            if self.j_type == conf.SHOULDER_REAR and self.servo.angle > conf.CRAWLY_REAR_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle - increment)
                return True # The shoulder is within the safe range.
            return False # The limit of movement is reached. 
        else:
            if self.j_type == conf.SHOULDER_FRONT and self.servo.angle < 180 - conf.CRAWLY_FRONT_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle + increment)
                return True # The shoulder is within the safe range.
            if self.j_type == conf.SHOULDER_REAR and self.servo.angle < 180 - conf.CRAWLY_REAR_BACKWARD_ANGLE:
                self.servo.set_angle(self.servo.angle + increment)
                return True # The shoulder is within the safe range.
            return False # The limit of movement is reached. 
        

    def park(self):
        '''Park the leg e.g. stretch it. '''
        if self.j_type == conf.KNEE:
            self.servo.set_angle(self.min_angle)
        elif self.j_type == conf.SHOULDER_FRONT:
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
        '''Curl the leg e.g. go to smallest position.'''
        if self.j_type == conf.KNEE:
            self.servo.set_angle(self.max_angle)
        elif self.j_type == conf.SHOULDER_FRONT or self.j_type == conf.SHOULDER_REAR:
            self.servo.set_angle(90)
                
    def tap(self):
        '''If this joint is a knee, it is tapped three times.'''
        if self.j_type == conf.KNEE:
            for i in range(3):
                self.servo.set_angle(85)
                sleep_ms(70)
                self.servo.set_angle(70)
                sleep_ms(70)
            
    def calibrate(self):
        '''Set all angles to 90°, so the legs can be attached correctly.  The joints are first moved to 0°, so ist can be
        checked, that they can move.'''
        self.servo.set_angle(0)
        sleep_ms(500)
        self.servo.set_angle(90)
        
    def __set_angle(self,a):
        if not self.left_side:
            self.servo.set_angle(a)
            #print(f"Winkel rechts: {a}") # Uncomment for debug messages.
        else:
            self.servo.set_angle(180-a)
            #print(f"Winkel links: {180-a}") # Uncomment for debug messages.
        
def main():    
    '''Executed, this sets all servos to 90°.'''
    j = Joint(conf.KNEE, "rear left", True, True, 1)
    j.calibrate()
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
