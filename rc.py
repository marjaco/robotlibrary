# Version 1.90
########## Import the configuration
from robotlibrary import config as conf
from robotlibrary.rotary import Rotary


########## Import bluetooth library
from robotlibrary.bluetooth.central import BLECentral
from robotlibrary.bluetooth.ble_services_definitions import MOTOR_TX_UUID, MOTOR_RX_UUID, ROBOT_UUID
from robotlibrary.bluetooth.parser import encode_motor, decode_motor

########## Import pico micropython libraries
import utime
from machine import Timer,ADC
import micropython
micropython.alloc_emergency_exception_buf(100)

class RC:
    '''This class represents the remote control with two rotary encoders and a slider to set the speed. Don't edit unless you know what you are doing. '''
    def __init__(self):
        self.forward = True
        self.speed = 0
        self.turn_val = 0 # 0=straight on; >0=turn right; <0=turn left
        self.change = True
        self.rotary_top = Rotary(18,19,16,self)
        self.rotary_bottom = Rotary(20,21,17,self)
        self.timer = Timer()
        self.timer.init(mode=Timer.PERIODIC, period=20, callback=self.set_speed)
        self.send_timer = Timer()
        self.send_timer.init(mode=Timer.PERIODIC, period=200, callback=self.send)
        self.duty_cycle = 0
        self.p = ADC(28)
        self.server = BLECentral(conf.ROBOT_NAME, True)
        self.server.register_read_callback(MOTOR_TX_UUID, self.read)
        self.server.scan()
        print("waiting for connection")
        while not self.server.is_connected():
            utime.sleep(1)
        utime.sleep(5)
        print("Found connection")
            
    def read(self,a):
        print("read")
    
    def send(self,t):
        if self.change: 
            #print("sending data ...")
            data = encode_motor(self.speed, self.turn_val, self.forward, 0)
            self.server.send(ROBOT_UUID, MOTOR_RX_UUID, data)
            self.change = False
    
    def rotary_changed(self,change):
        '''This is called when the direction knob is turned to determine the turn or spin. '''
        self.change = True
        if change == Rotary.ROT_CW: # Rotary encoder turned clockwise.
            self.turn_val = self.turn_val + 10
            if self.turn_val < 0:
                self.turn_val = 0            
        elif change == Rotary.ROT_CCW: # Rotary encoder turned anti-clockwise.
            self.turn_val = self.turn_val - 10
            if self.turn_val > 0:
                self.turn_val = 0
        elif change == Rotary.SW_RELEASE: # Button pressed.
            utime.sleep_ms(10)
            self.button()
            
    def button(self):
        '''This is the button click.'''
        self.forward = not self.forward
        self.change = True
                
    def set_speed(self,t):
        '''This calculates the speed between MIN_SPEED and MAX_SPEED that is sent to the robot.'''
        cycles = [0,0,0,0,0]
        sum=0
        for i in range(0,len(cycles)):
            cycles[i] = self.p.read_u16()
        for c in cycles:
            sum = sum + c
        dc = sum/5
        if dc > self.duty_cycle + 200 or dc < self.duty_cycle - 200:
            self.duty_cycle = dc    
            if dc > conf.MAX_DUTY:
                speed = conf.MAX_SPEED
            elif dc < conf.MIN_DUTY:
                speed = 0
            else: 
                speed = int((conf.MAX_SPEED/conf.MAX_DUTY*dc)*((conf.MAX_SPEED-conf.MIN_SPEED)/conf.MAX_SPEED)+conf.MIN_SPEED)
                print(speed)
            if speed != self.speed:
                self.speed = speed
                self.change = True

def main():
    rc = RC()
    while True:
        utime.sleep_ms(500)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()