# Version 2.0.1
from machine import Pin,Timer
from time import sleep
import micropython

micropython.alloc_emergency_exception_buf(100)

class IR:
    '''This class manages the IR-sensor. Calls Robot.ir_detected()'''
    def __init__(self, pinNo,robot):
        self.out = pinNo
        self.robot= robot
        self.ir = Pin(pinNo, Pin.IN, Pin.PULL_UP)
        self.ir.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.obstacle)
        self.detected=False
        self.timer = Timer()
        
    def reset_detected(self,t):
        self.detected = False
        
    def obstacle(self, pin):
        '''This is called on any change in the IR-sensor. '''
        if not self.detected:
            self.robot.ir_detected(pin,self.out)
            self.detected = True
            self.timer.init(mode=Timer.ONE_SHOT, period=100, callback=self.reset_detected)

    
def main(): 
    from robotlibrary.robot import Robot
    r = Robot(False)
    while True:
        sleep(1)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
            