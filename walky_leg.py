# Version 1.92
from robotlibrary.walky_joint import Joint
import robotlibrary.config_walky
from time import sleep

class Leg:
    def __init__(self, pin, right, front, name):
        if right: 
            self.hip = Joint(robotlibrary.config.walky_config.HIP, name, False, False, pin)
            self.knee = Joint(robotlibrary.config.walky_config.KNEE, name, False, False, pin+1)
        if not right:
            self.hip = Joint(robotlibrary.config.walky_config.HIP, name, True, False, pin)
            self.knee = Joint(robotlibrary.config.walky_config.KNEE, name, True, False, pin+1)
        
    def move_forward(self) -> bool:
#         walk = True
#         while self.knee.up():
#             pass
#         while self.shoulder.forward():
#             pass
#         return False
    
        w1 = self.knee.up()
        w2 = self.hip.forward()
        if not w2:
            self.knee.down()
        return w1 or w2
    def move_backward(self) -> bool:
        w1 = self.knee.down()
        w2 = self.hip.backward()
        return w1 or w2
    
#         while self.knee.down():
#             pass
#         while self.shoulder.backward():
#             pass
#         return False
    
    def park(self):
        self.knee.park()
        self.shoulder.park()
        
    def calibrate(self):
        self.hip.calibrate()
        self.knee.calibrate()
    
    def curl(self):
        self.knee.curl()
        self.shoulder.curl()
        
    def tap(self):
        self.knee.tap()
        
def main():
    l = Leg(4, True, False, "rear left")
    for i in range (10):
        while l.move_forward():
            pass
        while l.move_backward():
            pass
    
    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
