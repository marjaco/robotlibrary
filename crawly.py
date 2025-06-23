# peripherals
from robotlibrary.ultrasonic import Ultra
from robotlibrary.crawly_leg import Leg
from robotlibrary import config_crawly as conf
from robotlibrary.easing import get_factor, get_step
from time import sleep_ms

########## Bluetooth
# This is not implemented yet.
#BLUETOOTH_CHIP = FALSE
#import machine, sys, utime, random
from time import sleep


class Crawly:
    '''This is the central class which manages and uses all the other components of the robot.
    The parameters are defined in config_crawly.py'''
    def __init__(self,rc):
        self.legs = {
            "front_right" : Leg(4, True, True, "front right"),
            "rear_right" : Leg(6, True, False, "rear right"),
            "rear_left" : Leg(0, False, False, "rear left"),
            "front_left" : Leg(2, False, True, "front left")
            }
        if conf.US is not None:
            self.us = Ultra(conf.US)
            
    def move_to_start_pos(self):
        a_front = (conf.CRAWLY_FRONT_FORWARD_ANGLE + conf.CRAWLY_FRONT_BACKWARD_ANGLE) / 2
        a_rear = (conf.CRAWLY_REAR_FORWARD_ANGLE + conf.CRAWLY_REAR_BACKWARD_ANGLE) / 2
        self.legs["front_right"].shoulder.__set_angle(a_front)
        self.legs["rear_left"].shoulder.__set_angle(a_rear)
        self.legs["front_left"].shoulder.__set_angle(a_front)
        self.legs["rear_right"].shoulder.__set_angle(a_rear)
        
    def move_forward(self,steps,angle):
        '''Move the legs forward for one step at a time.'''
        #probably need to put the legs in a defined position first.
        # First step
        counter = 0 # counts the number of micro steps
        dividend=2 # fraction that determines when up or down motion is far enough to move the upper leg.
        knee_step=0 
        d=5 # wait for d milliseconds after each micro step
        factor = get_factor(steps,angle)
        while counter < steps/dividend:
            step = get_step(counter,steps,factor)
            self.legs["front_right"].leg_up(step)
            self.legs["rear_left"].leg_up(step)
            self.legs["front_left"].leg_down(step)
            self.legs["rear_right"].leg_down(step)
            sleep_ms(d)
            knee_step=counter
            counter+=1
        counter = 0
        while counter < steps:
            if counter < steps-knee_step:
                step = get_step(counter,steps+knee_step,factor)
                self.legs["front_right"].leg_up(step)
                self.legs["rear_left"].leg_up(step)
                self.legs["front_left"].leg_down(step)
                self.legs["rear_right"].leg_down(step)
            step = get_step(counter,steps,factor)
            self.legs["front_right"].leg_forward(step)
            self.legs["rear_left"].leg_forward(step)
            self.legs["front_left"].leg_backward(step)
            self.legs["rear_right"].leg_backward(step)
            sleep_ms(d)
            counter+=1

        # Second step
        counter = 0
        dividend=3
        knee_step=0
        factor = get_factor(steps,angle)
        while counter < steps/dividend:
            step = get_step(counter,steps,factor)
            self.legs["front_right"].leg_down(step)
            self.legs["rear_left"].leg_down(step)
            self.legs["front_left"].leg_up(step)
            self.legs["rear_right"].leg_up(step)
            sleep_ms(d)
            knee_step=counter
            counter+=1
        counter = 0
        while counter < steps:
            if counter < steps-knee_step:
                step = get_step(counter,steps+knee_step,factor)
                self.legs["front_right"].leg_down(step)
                self.legs["rear_left"].leg_down(step)
                self.legs["front_left"].leg_up(step)
                self.legs["rear_right"].leg_up(step)
            step = get_step(counter,steps,factor)
            self.legs["front_right"].leg_backward(step)
            self.legs["rear_left"].leg_backward(step)
            self.legs["front_left"].leg_forward(step)
            self.legs["rear_right"].leg_forward(step)
            sleep_ms(d)
            counter+=1
        
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
            l.calibrate()
        
    def tap(self):
        '''This taps all the legs. Looks and sounds scary and can also identify the legs.'''
        for l in self.legs.values():
            l.tap()
            sleep(0.1)
    
def main():
    try: 
        c = Crawly(False)
        c.move_to_start_pos()
        sleep(1)
        for i in range(0,10):
             c.move_forward(20,40+1)
        sleep(1)
        c.park()
    except KeyboardInterrupt:
        c.park()
        sleep(1)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
