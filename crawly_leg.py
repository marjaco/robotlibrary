from robotlibrary.crawly_joint import Joint
import robotlibrary.config
from time import sleep

class Leg:
    def __init__(self, pin, right, front, name):
        if right and front: 
            self.shoulder = Joint(robotlibrary.config.SHOULDER_FRONT, name, False, False, pin)
        if right and not front:
            self.shoulder = Joint(robotlibrary.config.SHOULDER_REAR, name, False, False, pin)
        if not right and front:
            self.shoulder = Joint(robotlibrary.config.SHOULDER_FRONT, name, True, False, pin)
        if not right and not front:
            self.shoulder = Joint(robotlibrary.config.SHOULDER_REAR, name, True, False, pin)
        self.knee = Joint(robotlibrary.config.KNEE, name, False, True, pin+1)
        
    def move_forward(self) -> bool:
        '''This makes a small adjustment in the move forward of this leg. Returns True as long as the movement is NOT finished
        and returns False, once the movement is finished. This does not move the robot forward, 
        as the leg is raised in this movement.
        '''
        w1 = self.knee.up()
        w2 = self.shoulder.forward()
        return w1 or w2
    
    def move_backward(self) -> bool:
        '''This makes a small adjustment in the move backward of this leg. Returns True as long as the movement is NOT finished
        and returns False, once the movement is finished. This does actually move the robot forward, 
        as the leg is lowered.
        '''
        w1 = self.knee.down()
        w2 = self.shoulder.backward()
        return w1 or w2
    
    
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
    l = Leg(6, False, False, "rear left")
    l.calibrate()
    
if __name__ == "__main__":
    # execute only if run as a script
    main()