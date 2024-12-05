from robotlibrary.joint import Joint
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
#         walk = True
#         while self.knee.up():
#             pass
#         while self.shoulder.forward():
#             pass
#         return False
    
        w1 = self.knee.up()
        w2 = self.shoulder.forward()
        return w1 or w2
    def move_backward(self) -> bool:
        w1 = self.knee.down()
        w2 = self.shoulder.backward()
        return w1 or w2
    
#         while self.knee.down():
#             pass
#         while self.shoulder.backward():
#             pass
#         return False
    
    def park(self):
        self.knee.park()
        self.shoulder.park()
        

def main():
    l = Leg(0, False, False, "rear left")
    for i in range(5):
        l.move_forward()
#     legs = [Leg(4, True, True, "front right"), Leg(2, False, True, "front left"),Leg(6, True, False, "rear right"), Leg(0, False, False, "rear left")]
#     legs[0].shoulder.move_forward()
#     legs[3].shoulder.move_backward()
#     for l in legs:
#         l.move_forward()
#     for l in legs:
#         pass
#         l.park()
#     for l in legs:
#         l.knee.down()
        
    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()