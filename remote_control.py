from machine import Pin, ADC
from robotlibrary.rotary import Rotary
import utime
from time import sleep
from central import BLECentral
from ble_services_definitions import MOTOR_RX_UUID, ROBOT_UUID, MOTOR_TX_UUID
from parser import encode_motor

forward = True
speed = 0
rotary_top = Rotary(18,19,16)
rotary_bottom = Rotary(20,21,17)
val = 0
right = False
left = False
changes = True
def rotary_changed(change):
    global val,right,left, changes
    if change == Rotary.ROT_CW:
        val = val + 1
        #print(val)
        if val > 0:
            right=True
            left = False
            current_status["left_speed"] -= val * 5
            current_status["right_speed"] += val * 5
        elif val == 0:
            right,left = False,False
        changes = True
    elif change == Rotary.ROT_CCW:
        val = val - 1
        #print(val)
        if val < 0:
            left = True
            right = False
            current_status["left_speed"] += val * 5
            current_status["right_forward"] -= val * 5
        elif val == 0:
            right,left = False,False
        changes = True
    elif change == Rotary.SW_PRESS:
        #print('PRESS')
        pass
    elif change == Rotary.SW_RELEASE:
        #print('RELEASE')
        utime.sleep_ms(10)
        toggle_direction()
    #send_motor_command()
        
current_status = {
    "left_speed": 0,
    "right_speed": 0,
    "left_forward": True,
    "right_forward": True
}

def toggle_direction():
    global forward
    forward = not forward
    current_status["left_forward"] = not current_status["left_forward"]
    current_status["right_forward"] = not current_status["right_forward"]
    changes = True
    
def set_speed(s):
    global speed
    if s >65100:
        speed = 255
    elif s < 400:
        speed = 0
    else: 
        speed = int(255/65535*s)
    #current_status["left_speed"] = speed
    #current_status["right_speed"] = speed
    #send_motor_command()

    

def read():
    pass

p = ADC(28)
#b = Pin(14, Pin.IN, Pin.PULL_UP)
#b.irq(trigger=Pin.IRQ_FALLING, handler=toggle_direction)
direction_pin = Pin(16, Pin.IN, Pin.PULL_UP)
step_pin = Pin(17, Pin.IN, Pin.PULL_UP)
duty_cycle = 0

# server = BLECentral(True)
# server.register_read_callback(MOTOR_TX_UUID, read)
# 
# def send_motor_command():
#     data = encode_motor(current_status["left_forward"], current_status["right_forward"], current_status["left_speed"],
#                         current_status["right_speed"])
#     server.send(ROBOT_UUID, MOTOR_RX_UUID, data)
# 
# 
# server.scan()
# 
# print("waiting for connection")
# while not server.is_connected():
#     sleep(1)
# 
# sleep(4)

rotary_top.add_handler(rotary_changed)
rotary_bottom.add_handler(rotary_changed)
print("Found connection")

cycles = [0,0,0,0,0]


while True:
    sum=0
    #dc = p.read_u16()
    for i in range(0,len(cycles)):
        cycles[i] = p.read_u16()
    for c in cycles:
        sum = sum + c
    
    dc = sum/5
    
    if dc > duty_cycle + 200 or dc < duty_cycle - 200 or changes:
        changes = False
        duty_cycle = dc
        set_speed(dc)
        if forward and right :
            print("Speed: ",speed, " ↑→")
        elif forward and left:
            print("Speed: ",speed, " ←↑")
        elif forward and not right and not left:
            print("Speed: ",speed, " ↑")
        elif not forward and right :
            print("Speed: ",speed, " ↓→")
        elif not forward and left:
            print("Speed: ",speed, " ←↓")
        elif not forward and not right and not left:
            print("Speed: ",speed, " ↓")
    utime.sleep_ms(50)