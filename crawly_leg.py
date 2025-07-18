# Version 1.92
from robotlibrary.crawly_joint import Joint
from robotlibrary import config_crawly as conf
from time import sleep,sleep_ms
from robotlibrary.easing import get_factor, get_step

class Leg:
    def __init__(self, pin, right, front, name):
        if right and front: 
            self.shoulder = Joint(conf.SHOULDER_FRONT, name, False, False, pin)
        if right and not front:
            self.shoulder = Joint(conf.SHOULDER_REAR, name, False, False, pin)
        if not right and front:
            self.shoulder = Joint(conf.SHOULDER_FRONT, name, True, False, pin)
        if not right and not front:
            self.shoulder = Joint(conf.SHOULDER_REAR, name, True, False, pin)
        self.knee = Joint(conf.KNEE, name, False, True, pin+1)
    
    def leg_up(self, inc):
        return self.knee.up_step(inc)

    def leg_down(self,inc):
        return self.knee.down_step(inc)

    def leg_forward(self,inc):
        return self.shoulder.forward_step(inc) 

    def leg_backward(self,inc):
        return self.shoulder.backward_step(inc)
    
    def get_angles(self):
        return f"Shoulder angle; {self.shoulder.servo.angle}; Knee angle; {self.knee.servo.angle}"
    
    def park(self):
        '''This streteches the leg.'''
        self.knee.park()
        self.shoulder.park()
        
    def calibrate(self):
        '''This sets all the servos to 90°'''
        self.knee.calibrate()
        self.shoulder.calibrate()
    
    def curl(self):
        '''This bends the knees and sets the shoulder to 90°.'''
        self.knee.curl()
        self.shoulder.curl()
        
    def tap(self):
        '''Taps the leg.'''
        self.knee.tap()
        
        
def main():
    '''This file, executed, taps the leg.'''
    l = Leg(6, True, False, "rear right")
    l.curl()
    sleep_ms(400)
    l.park()

    
if __name__ == "__main__":
    # execute only if run as a script
    main()
