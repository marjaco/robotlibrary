# Version 2.0.1
########## Import the configuration
from robotlibrary import config as conf
from robotlibrary.rotary import Rotary
from robotlibrary.joystick import Joystick

########## Import bluetooth library
from robotlibrary.bluetooth.central import BLECentral
from robotlibrary.bluetooth.ble_services_definitions import MOTOR_TX_UUID, MOTOR_RX_UUID, ROBOT_UUID
from robotlibrary.bluetooth.parser import encode_motor, decode_motor

########## Import pico micropython libraries
from time import sleep, sleep_ms
from machine import Timer,ADC
import micropython
micropython.alloc_emergency_exception_buf(100)

class RC:
    '''This class represents the remote control with two rotary encoders and a slider to set the speed. Don't edit unless you know what you are doing. '''
    def __init__(self):
        self.forward = True
        self.speed = 0
        self.turn_val = 0 # 0=straight on; >0=turn right; <0=turn left
        self.button_pressed = False
        #self.change = True
        self.joystick = Joystick(conf.X_PIN,conf.Y_PIN,conf.B_PIN) # Pins for x axis, y axis and button
        self.timer = Timer()
        self.timer.init(mode=Timer.PERIODIC, period=50, callback=self.set_values)
        self.send_timer = Timer()
        self.send_timer.init(mode=Timer.PERIODIC, period=200, callback=self.send)
        self.duty_cycle = 0
        self.server = BLECentral(conf.ROBOT_NAME, True)
        self.server.register_read_callback(MOTOR_TX_UUID, self.read)
        self.server.scan()
        self.button_pressed_sent = False
        print("waiting for connection")
        while not self.server.is_connected():
            sleep(1)
        sleep(5)
        print("Found connection")
            
    def read(self,a):
        print("read")
    
    def get_button_pressed(self):
        if self.button_pressed_sent == False and self.button_pressed:
            return True
        sleep_ms(20)
        self.button_pressed_sent = False
        return False
    
    def send(self,t): 
        print(f"sending data ... speed: {self.speed}, turn: {self.turn_val}, forward: {self.forward}, button: {self.get_button_pressed()}")
        data = encode_motor(self.speed, self.turn_val, self.forward, self.get_button_pressed())
        self.server.send(ROBOT_UUID, MOTOR_RX_UUID, data)
        if self.button_pressed:
            self.button_pressed_sent = True
                
    def set_values(self,t): 
        '''This calculates the speed between MIN_SPEED and MAX_SPEED that is sent to the robot.'''
        s = self.joystick.get_speed()
        self.speed = abs(s)
        self.turn_val = self.joystick.get_direction()
        self.forward = s >= 0
        self.button_pressed = self.joystick.pressed
        
def main():
    rc = RC()
    while True:
        sleep_ms(500)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()

