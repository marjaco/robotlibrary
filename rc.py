from robotlibrary.config import MIN_DUTY, MAX_DUTY, MAX_SPEED, MIN_SPEED
from robotlibrary.rotary import Rotary
import utime
from time import sleep
from robotlibrary.bluetooth.central import BLECentral
from robotlibrary.bluetooth.ble_services_definitions import MOTOR_TX_UUID, MOTOR_RX_UUID, ROBOT_UUID
from robotlibrary.bluetooth.parser import encode_motor, decode_motor
from machine import Timer,ADC
class RC:
    
    def __init__(self):
        self.forward = True
        self.speed = 0
        self.val = 0
        self.rotary_top = Rotary(18,19,16,self)
        self.rotary_bottom = Rotary(20,21,17,self)
        self.timer = Timer()
        self.timer.init(mode=Timer.PERIODIC, period=20, callback=self.set_speed)
        self.send_timer = Timer()
        self.send_timer.init(mode=Timer.PERIODIC, period=2000, callback=self.send)
        self.duty_cycle = 0
        self.p = ADC(28)
        self.server = BLECentral(True)
        self.server.register_read_callback(MOTOR_TX_UUID, self.read)
        self.server.scan()
        print("waiting for connection")
        while not self.server.is_connected():
            sleep(1)
        sleep(5)
        print("Found connection")

#         while True:
#             text = input("Please input in format: left_forward, right_forward, left_speed, right_speed: ")
#             [left_forward, right_forward, left_speed, right_speed] = text.split(", ")
#             left_forward, right_forward, left_speed, right_speed = (left_forward == "True", right_forward == "True",
#                                                                     int(left_speed), int(right_speed))
#             print(left_forward, right_forward)
            
    def read(self,a):
        print("read")
    
    def send(self,t):
        print("sending data ...")
        data = encode_motor(self.speed, self.val, self.forward)
        self.server.send(ROBOT_UUID, MOTOR_RX_UUID, data)
    
    def rotary_changed(self,change):
        if change == Rotary.ROT_CW: # Rotary encoder turned clockwise.
            self.val = self.val + 1
            if self.val > 0:
                print("go right")
                #current_status["left_speed"] -= self.val * 5
                #current_status["right_speed"] += self.val * 5
            else: # We are back to straight on.
                self.val = 0
                print("go straight")
                # go straight on
            
        elif change == Rotary.ROT_CCW: # Rotary encoder turned anti-clockwise.
            self.val = self.val - 1
            
            if self.val < 0:
                print("go left")
                #current_status["left_speed"] += self.val * 5
                #current_status["right_forward"] -= self.val * 5
            else:
                self.val = 0
                print("go straight")
                # go straight on
        elif change == Rotary.SW_RELEASE: # Button pressed.
            utime.sleep_ms(10)
            self.button()
            
    def button(self):
        self.forward = not self.forward
        #current_status["left_forward"] = not current_status["left_forward"]
        #current_status["right_forward"] = not current_status["right_forward"]
        print("toggle direction")
        
    def set_speed(self,t):
        cycles = [0,0,0,0,0]
        sum=0
        for i in range(0,len(cycles)):
            cycles[i] = self.p.read_u16()
        for c in cycles:
            sum = sum + c
        dc = sum/5
        if dc > self.duty_cycle + 200 or dc < self.duty_cycle - 200:
            self.duty_cycle = dc    
            if dc > MAX_DUTY:
                speed = MAX_SPEED
            elif dc < MIN_DUTY:
                speed = 0
            else: 
                speed = int(MAX_SPEED/MAX_DUTY*dc)
            if speed != self.speed:
                self.speed = speed
                print(self.speed)
        #current_status["left_speed"] = speed
        #current_status["right_speed"] = speed
        #send_motor_command()

def main():
    rc = RC()
    while True:
        utime.sleep_ms(500)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()