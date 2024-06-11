from robotlibrary.motor import Motor
from robotlibrary.ultrasonic import Ultra
from robotlibrary.infrared import IR
from robotlibrary.servo import Servo
# Version 1.0
import utime, random
class Robot:
    '''Initialize the class.
        The parameters are in this order: 
        motor_left = First pin for left motor, f.ex. 12
        motor_right = First pin for right motor, f. ex 14
        us = First pin for ultrasonic sensor, f. ex. 16
        ir = Pin for IR-sensor, f. ex. 11
        servo = Pin for servo motor, f. ex. 9
        Motors and ultrasonic sensor must use consecutive pins.'''
    def __init__(self,ml,mr,us,ir,s):
        self.motor_left = Motor(ml)
        self.motor_right = Motor(mr)
        if us >= 0:
            self.us = Ultra(us)
        if ir >= 0:
            self.ir = IR(ir,self)
        if s >=0:
            self.servo = Servo(s,self)
        self.speed = 0
        self.new_speed = 0
        self.last_turn_right = random.randint(0,1) == 0
#     def __init__(self,elements):
#         for key in elements: 
#             self.key = elements[key]
#             print(key)
#         self.speed = 0
#         self.new_speed = 0
#         self.last_turn_right = random.randint(0,1) == 0
    
    def drive(self, dir_l, dir_r):
        '''This abstracted driving function is only called locally by the other functions with better names. '''
        print("alte_G: ", self.speed, " neue G: ", self.new_speed)
        self.motor_left.set_forward(dir_l)
        self.motor_right.set_forward(dir_r)
        if self.new_speed < self.speed:
            steps = -1
        else:
            steps = 1
        for i in range(self.speed,self.new_speed,steps):
            self.motor_left.set_speed(i)
            self.motor_right.set_speed(i)
            utime.sleep_ms(10+int(i/2))
        self.speed = self.new_speed
        
    def drive_instantly(self,dir_l,dir_r):
        self.motor_left.set_forward(dir_l)
        self.motor_right.set_forward(dir_r)
        self.motor_left.set_speed(self.new_speed)
        self.motor_right.set_speed(self.new_speed)
        self.speed = self.new_speed
        
    def set_speed(self,s):
        '''Sets the new speed. Has to be set before
        other driving functions when changing the speed of the robot. '''
        self.new_speed = s
        
    def forward(self):
        '''Drive forward. Speed has to be set before with set_speed()'''
        self.drive(True, True)
        
    def backward(self):
        '''Drive forward. Speed has to be set before with set_speed()'''
        self.drive(False, False)

    def turn_right(self, d):
        '''Turn right for the given duration. We cannot determine the angle the robot turns without a compass or gyroscope.'''
        self.drive_instantly(True,False)
        utime.sleep_ms(d)
        self.emergency_stop()
        
    def turn_before_obstacle(self, distance):
        self.drive(True,False)
        while self.get_dist() < distance:
            pass
        self.emergency_stop()
            
    def turn_left(self, d):
        '''Turn right for the given duration. We cannot determine the angle the robot turns without a compass or gyroscope.'''
        self.drive_instantly(False,True)
        utime.sleep_ms(d)
        self.emergency_stop()
        
    def toggle_turn(self, d):
        '''Toggle turn for the given duration. We cannot determine the angle the robot turns without a compass or gyroscope.'''
        if self.last_turn_right:
            self.turn_left(d)
        else:
            self.turn_right(d)
        self.last_turn_right = not self.last_turn_right
    
    
    def random_turn(self,d):
        '''Randomly turn for the given duration. We cannot determine the angle the robot turns without a compass or gyroscope.'''
        if random.randint(0,1) == 0:
            self.turn_left(d)
        else:
            self.turn_right(d)
                
    def stop(self):
        '''Stop the robot slowly by deceleration. '''
        self.set_speed(0)
        self.drive(self.motor_left.forward, self.motor_right.forward)
        
    def emergency_stop(self):
        '''Stop the robot immediately.'''
        self.motor_left.set_speed(0)
        self.motor_right.set_speed(0)
        # self.set_speed(0)
        self.speed = 0
    
    def obstacle_detected(self, pin, pin_num):
        '''This method is called when the IR-sensor has detected a change. Fill in your code accordingly'''
        if pin.value() == 0:
            print("obstacle detected on pin", pin_num)
        else:
            print("There is no obstacle anymore on pin ", pin_num)
        # self.emergency_stop()
        
    def get_dist(self):
        return self.us.get_dist()

    def set_angle(self,a):
        self.servo.set_angle(a)
    
    def get_smallest_distance(self):
        '''This returns the angle of the ultrasonic sensor where it measured the smallest distance'''
        self.set_angle(0)
        utime.sleep_ms(500)
        dist_map = {}
        smallest_index=0
        smallest_dist=2000.0
        for i in range(0,180):
            self.set_angle(i)
            dist_map.update({i : self.get_dist()})
        for i,dist in dist_map.items():
            if dist<smallest_dist:
                smallest_index=i
                smallest_dist=dist
        return smallest_index+1

    def get_longest_distance(self):
        '''This returns the angle of the ultrasonic sensor where it measured the longest distance'''
        self.set_angle(0)
        utime.sleep_ms(500)
        dist_map = {}
        longest_index=0
        longest_dist=0.0
        for i in range(0,180):
            self.set_angle(i)
            dist_map.update({i : self.get_dist()})
        for i,dist in dist_map.items():
            if dist>longest_dist:
                longest_index=i
                longest_dist=dist
        return longest_index+1
        
        
