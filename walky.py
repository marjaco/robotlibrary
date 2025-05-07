# peripherals
#from robotlibrary.motor import Motor
from robotlibrary.ultrasonic import Ultra
#from robotlibrary.infrared import IR
from robotlibrary.walky_leg import Leg
import robotlibrary.config_walky

########## Bluetooth
import bluetooth
from robotlibrary.bluetooth.peripheral import BLEPeripheral
from robotlibrary.bluetooth.ble_services_definitions import ROBOT_UUID, MOTOR_RX_UUID, MOTOR_TX_UUID
from robotlibrary.bluetooth.parser import decode_motor, encode_motor

import machine, sys, utime, random
from time import sleep


class Walky:
    '''This is the central class which manages and uses all the other components of the robot. The parameters are defined in config.py'''
    def __init__(self,rc):
#         self.front_right = Leg(4, True, True, "front right")
#         self.front_left = Leg(2, False, True, "front left")
#         self.rear_right = Leg(6, True, False, "rear right")
#         self.rear_left = Leg(0, False, False, "rear left")
        self.legs = {
            "front_right" : Leg(4, True, True, "front right"),
            "rear_right" : Leg(6, True, False, "rear right"),
            "rear_left" : Leg(0, False, False, "rear left"),
            "front_left" : Leg(2, False, True, "front left")
            }
        if robotlibrary.config.walky_config.US is not None:
            self.us = Ultra(robotlibrary.config.walky_config.US)
        
        
    
    def move_forward(self):
        '''This makes the crawler move forward in a coordinated way. Most of the funktionality lies in the other classes Joint and Leg'''
        while True:
            walk = True
            while walk:
                w1 = self.legs["front_right"].move_forward()
                w2 = self.legs["rear_left"].move_forward()
                w3 = self.legs["rear_right"].move_backward()
                w4 = self.legs["front_left"].move_backward()
                walk = w1 or w2 or w3 or w4
            
            walk = True
            while walk:
                w1 = self.legs["front_right"].move_backward()
                w2 = self.legs["rear_left"].move_backward()
                w3 = self.legs["rear_right"].move_forward()
                w4 = self.legs["front_left"].move_forward()
                
                walk = w1 or w2 or w3 or w4
            
            
    def park(self):
        self.front_right.park()
        self.front_left.park()
        self.rear_right.park()
        self.rear_left.park()
        
    def curl(self):
        self.front_right.curl()
        self.front_left.curl()
        self.rear_right.curl()
        self.rear_left.curl()
    
    def calibrate(self):
        for l in self.legs.values():
            l.calibrate()
        
    def tap(self, leg):
        leg.tap()
    
def main(): 
    w = Walky(False)
    w.calibrate()
    
if __name__ == "__main__":
    # execute only if run as a script
    main()

