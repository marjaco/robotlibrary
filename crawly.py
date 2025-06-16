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
    '''This is the central class which manages and uses all the other components of the robot. The parameters are defined in config_crawly.py'''
    def __init__(self,rc):
        self.legs = {
            "front_right" : Leg(4, True, True, "front right"),
            "rear_right" : Leg(6, True, False, "rear right"),
            "rear_left" : Leg(0, False, False, "rear left"),
            "front_left" : Leg(2, False, True, "front left")
            }
        if conf.US is not None:
            self.us = Ultra(conf.US)
            
  
    def reset_movement(self):
        '''This needs to be called before each new movement of a leg. '''
        for l in self.legs.values():
            l.reset_movement()
    
    def move_forward(self,steps,angle):
        #angle=50
        #steps=15
        print("start")
        counter = 0
        dividend=3
        knee_step=0
        d=80
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
        #c.calibrate()
        c.curl()
        for i in range(0,10):
             c.move_forward(20,30)
        sleep(1)
        c.park()
    except KeyboardInterrupt:
        c.park()
        sleep(1)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
