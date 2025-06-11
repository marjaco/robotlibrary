from robotlibrary.crawly_joint import Joint
from robotlibrary import config_crawly as conf
from time import sleep,sleep_ms

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
    
    @deprecated
    def reset_movement(self):
        '''This needs to be called before the leg starts moving.'''
        self.shoulder.reset_movement()
        self.knee.reset_movement()
        
    def forward_move_forward(self) -> bool:
        '''This makes a small adjustment in the move forward of this leg. Returns True as long as the movement is NOT finished
        and returns False, once the movement is finished. This does not move the robot forward, 
        as the leg is raised in this movement.
        '''
        w1,w2 = True,True
        w1 = self.knee.up_smooth_v2()
        if not w1:
            w2 = self.shoulder.forward()
        return w1 or w2
    
    def forward_move_backward(self) -> bool:
        '''This makes a small adjustment in the move backward of this leg. Returns True as long as the movement is NOT finished
        and returns False, once the movement is finished. This does actually move the robot forward, 
        as the leg is lowered.
        '''
        w1,w2 = True,True
        w1 = self.knee.down_smooth_v2()
        if not w1:
            w2 = self.shoulder.backward()
        return w1 or w2
    

    def backward_move_forward(self) -> bool:
        '''This makes a small adjustment in the move forward of this leg. Returns True as long as the movement is NOT finished
        and returns False, once the movement is finished. This does not move the robot backward, 
        as the leg is lowered.
        '''
        w1 = self.knee.down()
        w2 = self.shoulder.forward()
        return w1 or w2
    
    def backward_move_backward(self) -> bool:
        '''This makes a small adjustment in the move backward of this leg. Returns True as long as the movement is NOT finished
        and returns False, once the movement is finished. This does actually move the robot backward, 
        as the leg is raised in this movement.
        '''
        w1 = self.knee.up()
        w2 = self.shoulder.backward()
        return w1 or w2
    


    def left_move_ahead(self) -> bool:
        '''This makes the leg go to the very front or very back of the robot depended on the position of the shoulder.
        The knee is raised or lowered depended on the side where it is mounted on.
        This is used to move the robot to the left.
        '''
        if self.right:
            w1 = self.knee.side_walking_up()
        else:
            w1 = self.knee.side_walking_down()
        w2 = self.shoulder.ahead()
        return w1 or w2
    
    def left_move_center(self) -> bool:
        '''This makes the leg go to the center, which means setting the servo on 90 degrees.
        The knee is raised or lowered depended on the side where it is mounted on.
        This is used to move the robot to the left.
        '''
        if self.right:
            w1 = self.knee.side_walking_down()
        else:
            w1 = self.knee.side_walking_up()
        w2 = self.shoulder.center()
        return w1 or w2
    

    def right_move_ahead(self) -> bool:
        '''This makes the leg go to the very front or very back of the robot depended on the position of the shoulder.
        The knee is raised or lowered depended on the side where it is mounted on.
        This is used to move the robot to the right.
        '''
        if self.right:
            w1 = self.knee.side_walking_down()
        else:
            w1 = self.knee.side_walking_up()
        w2 = self.shoulder.ahead()
        return w1 or w2
 
    def right_move_center(self) -> bool:
        '''This makes the leg go to the center, which means setting the servo on 90 degrees.
        The knee is raised or lowered depended on the side where it is mounted on.
        This is used to move the robot to the right.
        '''
        if self.right:
            w1 = self.knee.side_walking_up()
        else:
            w1 = self.knee.side_walking_down()
        w2 = self.shoulder.center()
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
    l = Leg(6, True, False, "rear right")
    l.park()
    l.knee.down()
    l.reset_movement()
    
    while l.forward_move_forward():
        sleep_ms(200)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
