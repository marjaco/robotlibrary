# peripherals
from robotlibrary.ultrasonic import Ultra
from robotlibrary.crawly_leg import Leg
import robotlibrary.config

########## Bluetooth
# This is not implemented yet.
import bluetooth
from robotlibrary.bluetooth.peripheral import BLEPeripheral
from robotlibrary.bluetooth.ble_services_definitions import ROBOT_UUID, MOTOR_RX_UUID, MOTOR_TX_UUID
from robotlibrary.bluetooth.parser import decode_motor, encode_motor

#import machine, sys, utime, random
from time import sleep


class Crawly:
    '''This is the central class which manages and uses all the other components of the robot. The parameters are defined in config.py'''
    def __init__(self,rc):
        self.legs = {
            "front_right" : Leg(4, True, True, "front right"),
            "rear_right" : Leg(6, True, False, "rear right"),
            "rear_left" : Leg(0, False, False, "rear left"),
            "front_left" : Leg(2, False, True, "front left")
            }
        if robotlibrary.config.US is not None:
            self.us = Ultra(robotlibrary.config.US)
        
    
    def move_forward(self, steps):
        '''This makes the crawler move forward in a coordinated way. Most of the funktionality lies in the other classes Joint and Leg'''
        while steps > 0:
            walk = True
            # First half of one stepcycle.
            while walk:
                w1 = self.legs["front_right"].forward_move_forward()
                w2 = self.legs["rear_left"].forward_move_forward()
                w3 = self.legs["rear_right"].forward_move_backward()
                w4 = self.legs["front_left"].forward_move_backward()
                walk = w1 or w2 or w3 or w4
            
            walk = True
            # Second half of one stepcycle
            while walk:
                w1 = self.legs["front_right"].forward_move_backward()
                w2 = self.legs["rear_left"].forward_move_backward()
                w3 = self.legs["rear_right"].forward_move_forward()
                w4 = self.legs["front_left"].forward_move_forward()
                
                walk = w1 or w2 or w3 or w4
            steps = steps-1

    def move_backward(self, steps):
        '''This makes the crawler move backward in a coordinated way. Most of the funktionality lies in the other classes Joint and Leg'''
        while steps > 0:
            walk = True
            # First half of one stepcycle.
            while walk:
                w1 = self.legs["front_right"].backward_move_backward()
                w2 = self.legs["rear_left"].backward_move_backward()
                w3 = self.legs["rear_right"].backward_move_forward()
                w4 = self.legs["front_left"].backward_move_forward()
                walk = w1 or w2 or w3 or w4
            
            walk = True
            # Second half of one stepcycle
            while walk:
                w1 = self.legs["front_right"].backward_move_forward()
                w2 = self.legs["rear_left"].backward_move_forward()
                w3 = self.legs["rear_right"].backward_move_backward()
                w4 = self.legs["front_left"].backward_move_backward()
                
                walk = w1 or w2 or w3 or w4
            steps = steps-1


    def turn_left(self, steps):
        '''This makes the crawler turn to the left in on place in a coordinated way. Most of the funktionality lies in the other classes Joint and Leg'''
        while steps > 0:
            walk = True
            # First half of one stepcycle.
            while walk:
                w1 = self.legs["front_right"].forward_move_forward()
                w2 = self.legs["rear_left"].backward_move_backward()
                w3 = self.legs["rear_right"].forward_move_backward()
                w4 = self.legs["front_left"].backward_move_forward()
                walk = w1 or w2 or w3 or w4
            
            walk = True
            # Second half of one stepcycle
            while walk:
                w1 = self.legs["front_right"].forward_move_backward()
                w2 = self.legs["rear_left"].backward_move_forward()
                w3 = self.legs["rear_right"].forward_move_forward()
                w4 = self.legs["front_left"].backward_move_backward()
                
                walk = w1 or w2 or w3 or w4
            steps = steps-1

    def turn_right(self, steps):
        '''This makes the crawler turn to the right in on place in a coordinated way. Most of the funktionality lies in the other classes Joint and Leg'''
        while steps > 0:
            walk = True
            # First half of one stepcycle.
            while walk:
                w1 = self.legs["front_right"].backward_move_forward()
                w2 = self.legs["rear_left"].forward_move_backward()
                w3 = self.legs["rear_right"].backward_move_backward()
                w4 = self.legs["front_left"].forward_move_forward()
                walk = w1 or w2 or w3 or w4
            
            walk = True
            # Second half of one stepcycle
            while walk:
                w1 = self.legs["front_right"].backward_move_backward()
                w2 = self.legs["rear_left"].forward_move_forward()
                w3 = self.legs["rear_right"].backward_move_forward()
                w4 = self.legs["front_left"].forward_move_backward()
                
                walk = w1 or w2 or w3 or w4
            steps = steps-1

            
    def park(self):
        '''This stretches legs the legs lengthwise, so the robot lies on its underside.'''
        for l in self.legs.values():
            l.park()
        
    def curl(self):
        '''This movement bends the legs, so the robot stands on tiptoes.'''
        for l in self.legs.values():
            l.curl()
    
    def calibrate(self):
        '''This sets all servos to 90° so the legs can be assembled with the correct angles.'''
        for l in self.legs.values():
            l.calibrate
        
    def tap(self):
        '''This taps all the legs. Looks and sounds scary and can also identify the legs.'''
        for l in self.legs.values():
            l.tap()
            sleep(0.1)
    
def main():
    '''Starting this file calibrates all servos and then terminates.'''
    try: 
        c = Crawly(True)
        c.move_forward(10)
    except KeyboardInterrupt:
        c.park()
        sleep(1)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
