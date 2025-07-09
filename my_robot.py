# Version 1.90
from robotlibrary.robot import Robot
class MyRobot(Robot):
        
    def ir_detected(self, pin,pin_num):
        '''If the ir sensor detects something, this function is called.
        pin.value() == 0: White detected (there is a reflection)
        pin.value() == 1: Black detected (there is no reflection)'''
        pass
    