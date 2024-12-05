# peripherals
#from robotlibrary.motor import Motor
#from robotlibrary.ultrasonic import Ultra
#from robotlibrary.infrared import IR
from robotlibrary.servo_crab import Servo
import robotlibrary.config
from time import sleep

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
        self.servo = Servo(pin, inverted)
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
        else:
            return
        
        
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
    def __set_angle(self,a):
        if not self.left_side:
            self.servo.set_angle(a)
            print(f"Winkel rechts: {a}")
        else:
            self.servo.set_angle(180-a)
            print(f"Winkel links: {a}")
        
def main():
    
    j = Joint(robotlibrary.config.SHOULDER_REAR, "rear left", True, False, 0)
    j2 = Joint(robotlibrary.config.SHOULDER_REAR, "rear left", False, False, 6)
    j.__set_angle(120)
    j2.__set_angle(120)
    
    sleep(100)
    j2 = Joint(robotlibrary.config.SHOULDER_FRONT, "rear left", True, 2)
#     for i in range (30):
#         j.up()
#         j2.up()
    for i in range(3):
        walk = True
        while walk:
            w1=j.forward()
            w2=j2.forward()
            walk = w1 or w2
        print(f"{j.servo.angle}, {j2.servo.angle}")
        walk = True
        while walk:
            w1= j.backward()
            w2 = j2.backward()
            walk = w1 or w2
        sleep(1)
        print(f"{j.servo.angle}, {j2.servo.angle}")
    
    #j.park()
#     joints = [Joint(robotlibrary.config.KNEE,"left rear", False, 1), Joint(robotlibrary.config.KNEE,"left front", False, 3), Joint(robotlibrary.config.KNEE,"right_front", False, 5), Joint(robotlibrary.config.KNEE,"right_rear", False, 7) ]
#     sleep(2)
#     for j in joints:
#         j.move_up()
#         sleep(1)
#     for j in reversed(joints):
#         j.move_down()
#         sleep(1)    
#     for j in joints:
#         j.park()
#     j.park()
#     print(j.__dict__)
#     joints = [Joint(robotlibrary.config.SHOULDER_FRONT,"left front", True, 2), Joint(robotlibrary.config.SHOULDER_REAR,"left rear", True, 0),  Joint(robotlibrary.config.SHOULDER_FRONT,"right_front", False, 4), Joint(robotlibrary.config.SHOULDER_REAR,"right_rear", False, 6)]
#     sleep(2)
#     for j in joints:
#         j.move_forward()
#         sleep(1)
#     for j in reversed(joints):
#         j.move_backward()
#         sleep(1)    
#     for j in joints:
#         j.park()
#     j.park()
    print(j.__dict__)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()