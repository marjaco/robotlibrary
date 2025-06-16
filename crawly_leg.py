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
    
    def reset_movement(self):
        '''This needs to be called before the leg starts moving.'''
        print("This method is deprecated")
        self.shoulder.reset_movement()
        self.knee.reset_movement()
        
    def forward_move_forward(self) -> bool:
        '''This makes a small adjustment in the move forward of this leg. Returns True as long as the movement is NOT finished
        and returns False, once the movement is finished. This does not move the robot forward, 
        as the leg is raised in this movement.
        '''
        w1,w2 = True,True
        w1 = self.knee.up_smooth()
        if not w1:
            w2 = self.shoulder.forward()
        return w1 or w2
    
    def forward_move_forward_v3(self,increment) -> bool:
        '''This makes a small adjustment in the move forward of this leg. Returns True as long as the movement is NOT finished
        and returns False, once the movement is finished. This does not move the robot forward, 
        as the leg is raised in this movement.
        '''
        w1 = self.knee.up_smooth_v3(increment)
        w2 = self.shoulder.forward_v3(increment)
        return w1 or w2
    
    def forward_move_backward_v3(self,increment) -> bool:
        '''This makes a small adjustment in the move forward of this leg. Returns True as long as the movement is NOT finished
        and returns False, once the movement is finished. This does not move the robot forward, 
        as the leg is raised in this movement.
        '''
        w1 = self.knee.down_smooth_v3(increment)
        w2 = self.shoulder.backward_v3(increment)
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
    l.curl()
    steps=20
    angle=30
    d=50
    factor = get_factor(steps,angle)
    for i in range(0,steps):
        l.leg_up(get_step(i,steps,factor))
        sleep_ms(d)
    for i in range(0,steps):
        l.leg_forward(get_step(i,steps,factor))
        sleep_ms(d)
    for i in range(0,steps):
        l.leg_down(get_step(i,steps,factor))
        sleep_ms(d)
    for i in range(0,steps):
        l.leg_backward(get_step(i,steps,factor))
        sleep_ms(d)
    sleep_ms(200)
    l.park()

    
if __name__ == "__main__":
    # execute only if run as a script
    main()
