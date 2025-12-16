# Version 2.0.1
########## peripherals
from robotlibrary.motor import Motor
from robotlibrary.ultrasonic import Ultra
from robotlibrary.infrared import IR
from robotlibrary.servo import Servo
from robotlibrary.ir_array import IR_Array
from robotlibrary.pid import PID
from robotlibrary import config as conf

########## Bluetooth

try: 
    import bluetooth
    from robotlibrary.bluetooth.peripheral import BLEPeripheral
    from robotlibrary.bluetooth.ble_services_definitions import ROBOT_UUID, MOTOR_RX_UUID, MOTOR_TX_UUID
    from robotlibrary.bluetooth.parser import decode_motor, encode_motor
    BLUETOOTH_CHIP = True
except:
    BLUETOOTH_CHIP = False

import machine, sys, random
from machine import ADC
from time import sleep, sleep_ms


class Robot:
    '''This is the central class which manages and uses all the other components of the robot. The parameters are defined in config.py
    You can now also initiate the class with you own read() method, which takes the commands from the rc. '''
    def __init__(self,rc):
        self.mrf, self.mlf, self.ml, self.mr, self.us, self.ir, self.servo = None, None, None, None, None, None, None
        self.speed = 0
        self.forward = True
        self.new_speed = 0
        self.turn_value = 0
        self.last_turn_right = random.randint(0,1) == 0
        if conf.ML is not None:
            self.ml = Motor(conf.ML)
        if conf.MR is not None:
            self.mr = Motor(conf.MR)
        if conf.MRF is not None:
            self.mrf = Motor(conf.MRF)
        if conf.MLF is not None:
            self.mlf = Motor(conf.MLF)
        if conf.US is not None:
            self.us = Ultra(conf.US)
        if conf.IR is not None:
            self.ir = IR(conf.IR,self)
        if conf.SERVO is not None:
            self.servo = Servo(conf.SERVO, False, conf.SERVO_MIN_DUTY, conf.SERVO_MAX_DUTY)
        if conf.BATTERY is not None:
            self.battery = ADC(conf.BATTERY)
        if rc and BLUETOOTH_CHIP:
            self.rc_is_on = True
            self.controller = BLEPeripheral(conf.ROBOT_NAME, add_robot_stuff=True)
            def read(buffer: memoryview):
                speed, turn, forward, button_press = decode_motor(bytes(buffer))
                self.rc_input(speed, turn, forward, button_press)
            self.controller.register_read_callback(MOTOR_RX_UUID, read)
            self.controller.advertise()
            
    def rc_input(self, speed, turn, forward, button_press):
        ''' This method is called each time the remote control sends new data, which happens often.
        You can overwrite this method to implement your own control.
        '''
        #print(f"Speed: {speed}, Turn: {turn}, forward: {forward}, button_press: {button_press}") # uncomment for debugging
        if self.rc_is_on: 
            if forward != self.forward:
                self.forward = forward
                self.set_forward(forward)
            if speed != self.speed:
                self.set_speed_instantly(speed)                    
            if turn == 0:
                self.go_straight()
            elif turn < 0: 
                if turn < -50: # If a high value for turning is sent, then spin left on the spot. 
                    self.spin_left()
                else: # If a lower value for turning is sent, only turn slightly to the left. 
                    self.turn(turn)
            elif turn > 0:
                if turn > 50: # If a high value for turning is sent, then spin right on the spot. 
                    self.spin_right()
                else: # If a lower value for turning is sent, only turn slightly to the right. 
                    self.turn(turn)
            if turn > -20 and turn < 20: # Define the interval in the middle of the joystick which produces no turning. 
                self.set_forward(self.forward)
                self.go_straight()
            if button_press: # The button press has no default function. 
                print("Button pressed.")
                
    def rc_on(self):
        '''Can be used to switch the rc on or off if a combination of driving with rc and automatic driving
        is used, so the rc does not interfere with the automatic program. '''
        self.rc_is_on = True
        
    def rc_off(self):
        '''Can be used to switch the rc on or off if a combination of driving with rc and automatic driving
        is used, so the rc does not interfere with the automatic program. '''
        self.rc_is_on = False
        
    def _drive(self, dir_l, dir_r):
        '''This abstracted driving function is only called locally by the other functions with better names. 
        It accelerates and decelerates to make driving more natural. Do not call directly!'''
        self.ml.set_forward(dir_l)
        self.mr.set_forward(dir_r)
        if self.mrf is not None:
            self.mrf.set_forward(dir_r)
        if self.mlf is not None:
            self.mlf.set_forward(dir_l)
        if self.new_speed < self.speed:
            steps = -1
        else:
            steps = 1
        for i in range(self.speed,self.new_speed,steps):
            self.ml.set_speed(i)
            self.mr.set_speed(i)
            if self.mrf is not None:
                self.mrf.set_speed(i)
            if self.mlf is not None:
                self.mlf.set_speed(i)
            sleep_ms(10+int(i/2))
        self.speed = self.new_speed
        
    def _drive_instantly(self,dir_l,dir_r):
        '''This abstracted driving function is only called locally by the other functions with better names. 
        It sets the speed immediately. Do not call directly!'''
        self.ml.set_forward(dir_l)
        self.mr.set_forward(dir_r)
        self.ml.set_speed(self.new_speed)
        self.mr.set_speed(self.new_speed)
        if self.mrf is not None:
            self.mrf.set_forward(dir_l)
            self.mrf.set_speed(self.new_speed)
        if self.mlf is not None:
            self.mlf.set_forward(dir_l)
            self.mlf.set_speed(self.new_speed)
        self.speed = self.new_speed
        
    def set_speed_instantly(self,s):
        '''Sets the new speed immediately. Doesn't change the driving mode of the robot.
        :param s: the speed you want to set.'''
        self.speed = s
        self.new_speed = s
        self.ml.set_speed(self.new_speed)
        self.mr.set_speed(self.new_speed)
        if self.mrf is not None:
            self.mrf.set_speed(self.new_speed)
        if self.mlf is not None:
            self.mlf.set_speed(self.new_speed)
        
    def set_speed(self,s):
        '''Sets the new speed and accelerates and decelerates. Doesn't change the driving mode of the robot.
        :param s: the speed you want to set.'''
        self.new_speed = s
        if self.new_speed < self.speed:
            steps = -1
        else:
            steps = 1
        for i in range(self.speed,self.new_speed,steps):
            self.ml.set_speed(i)
            self.mr.set_speed(i)
            if self.mrf is not None:
                self.mrf.set_speed(i)
            if self.mlf is not None:
                self.mlf.set_speed(i)
            sleep_ms(10+int(i/2))
        self.speed = self.new_speed
        
    def set_forward(self,f):
        '''Sets the direction of the robot. True means forward.
        :param f: True for forwards and False for backwards.'''
        self.ml.set_forward(f)
        self.mr.set_forward(f)
        if self.mrf is not None:
            self.mrf.set_forward(f)
        if self.mlf is not None:
            self.mlf.set_forward(f)
        self.ml.set_speed(self.speed)
        self.mr.set_speed(self.speed)
        if self.mrf is not None:
            self.mrf.set_speed(self.speed)
        if self.mlf is not None:
            self.mlf.set_speed(self.speed)
        
    def spin_right(self):
        '''Spin right indefinitely. '''
        self.ml.reset_offset()
        self.mr.reset_offset()
        if self.mrf is not None:
            self.mrf.reset_offset()
        if self.mlf is not None:
            self.mlf.reset_offset()
        self._drive_instantly(True,False)
    
    def spin_left(self):
        '''Spin left indefinitely. '''
        self.ml.reset_offset()
        self.mr.reset_offset()
        if self.mrf is not None:
            self.mrf.reset_offset()
        if self.mlf is not None:
            self.mlf.reset_offset()
        self._drive_instantly(False,True)
        
    def turn_right(self):
        '''This turns the robot to the right without it spinning on the spot. Each call makes the turn steeper.'''
        self.ml.change_speed(5)
        self.mr.change_speed(-5)
        if self.mlf is not None:
            self.mlf.change_speed(5)
        if self.mrf is not None:
            self.mrf.change_speed(-5)
        
    def turn_left(self):
        '''This turns the robot to the right without it spinning on the spot. Each call makes the turn steeper.'''
        self.mr.change_speed(5)
        self.ml.change_speed(-5)
        if self.mlf is not None:
            self.mlf.change_speed(-5)
        if self.mrf is not None:
            self.mrf.change_speed(5)
    
    def turn(self,t):
        if turn <= self.turn_value - 4 or turn >= self.turn_value + 4:
            self.turn_value = turn
            self.mr.change_speed(t/-4)
            self.ml.change_speed(t/4)
            if self.mlf is not None:
                self.mlf.change_speed(t/4)
            if self.mrf is not None:
                self.mrf.change_speed(t/-4)
        
    def go_left(self):
        ''' With Meccanum wheels the robot goes sideways to the left.
        '''
        self.ml.set_forward(True)
        self.mlf.set_forward(False)
        self.mr.set_forward(False)
        self.mrf.set_forward(True)
        
    def go_right(self):
        ''' With Meccanum wheels the robot goes sideways to the right.
        '''
        self.ml.set_forward(False)
        self.mlf.set_forward(True)
        self.mr.set_forward(True)
        self.mrf.set_forward(False)
        
    def turn(self, turn):
        '''This turns the robot right or left. Is mostly used by the remote control.
        :param turn: positive or negative value. Higher values mean steeper turn.'''
        self.mr.change_speed(-turn)
        self.ml.change_speed(turn)
        if self.mrf is not None:
            self.mrf.change_speed(-turn)
        if self.mlf is not None:
            self.mlf.change_speed(turn)
        
    def go_straight(self):
        '''Lets the robot go straight on. Usually called when a turn shall end. '''
        self.ml.reset_offset()
        self.mr.reset_offset()
        if self.mrf is not None:
            self.mrf.reset_offset()
        if self.mlf is not None:
            self.mlf.reset_offset()
        self.ml.set_speed(self.speed)
        self.mr.set_speed(self.speed)
        if self.mrf is not None:
            self.mrf.set_speed(self.speed)
        if self.mlf is not None:
            self.mlf.set_speed(self.speed)
           
    def spin_before_obstacle(self, distance):
        '''This spins until the distance to an obstacle is greater than the given parameter *distance*.
        :param distance: The distance'''
        self._drive_instantly(True,False)
        while self.get_dist() < distance:
            pass
        self.emergency_stop()
                
    def toggle_spin(self, d):
        '''Toggle turn for the given duration. With each call the opposite direction(clockwise / anti-clockwise) is used.
        :param d: The duration for the turn in milliseconds.'''
        if self.last_turn_right:
            self.spin_left()
        else:
            self.spin_right()
        sleep_ms(d)
        self.emergency_stop()
        self.last_turn_right = not self.last_turn_right
    
    
    def random_spin(self,d):
        '''Randomly turn for the given duration.
        :param d: The duration for the turn in milliseconds.'''
        if random.randint(0,1) == 0:
            self.spin_left()
        else:
            self.spin_right()
        sleep_ms(d)
        self.emergency_stop()
                
    def stop(self):
        '''Stop the robot slowly by deceleration. '''
        self.set_speed(0)
        #self._drive(self.ml.forward, self.mr.forward)
        
    def emergency_stop(self):
        '''Stop the robot immediately.'''
        self.ml.set_speed(0)
        self.mr.set_speed(0)
        if self.mrf is not None:
            self.mrf.set_speed(0)
        if self.mlf is not None:
            self.mlf.set_speed(0)
        self.speed = 0
    
    def ir_detected(self, pin, pin_num):
        '''If implemented this method is called when the IR-sensor has detected a change. Fill in your code accordingly.'''
        if pin.value() == 0:
            print("obstacle detected on pin", pin_num)
        else:
            print("There is no obstacle anymore on pin ", pin_num)
        # self.emergency_stop()
        
    def get_dist(self):
        '''Get the distance from the ultrasonic sensor.'''
        return self.us.get_dist()

    def set_angle(self,a):
        '''If implemented, turn the servo motor with the ultrasonic sensor to the given angle.
        :param a: The angle that is to be set.'''
        self.servo.set_angle_slowly(a)
        
    def get_smallest_distance(self):
        '''This returns the angle of the ultrasonic sensor where it measured the smallest distance'''
        self.set_angle(0)
        sleep_ms(500)
        dist_map = {}
        smallest_index=0
        smallest_dist=2000.0
        for i in range(0,180):
            self.set_angle(i)
            dist_map.update({i : self.get_dist()})
        for i,dist in dist_map.items():
            if dist<smallest_dist:
                smallest_index=i
                smallest_dist=dist
        return smallest_index+1

    def get_longest_distance(self):
        '''This returns the angle of the ultrasonic sensor where it measured the longest distance'''
        self.set_angle(0)
        sleep_ms(500)
        dist_map = {}
        longest_index=0
        longest_dist=0.0
        for i in range(0,180):
            self.set_angle(i)
            dist_map.update({i : self.get_dist()})
        for i,dist in dist_map.items():
            if dist>longest_dist:
                longest_index=i
                longest_dist=dist
        return longest_index+1
    
    
    def follow_line(self): #unfinished
        pv = 0
        ir = IR_Array(0,5)
        pid = PID(ir, 0.01)
        self.set_speed(80)
        while True:
            control = int(round(pid.pid_controller()))
            pv += control * 0.01
            print(control)
            self.mr.set_speed(self.speed - control)
            self.ml.set_speed(self.speed + control)
            sleep_ms(10)
            
    def get_battery_charge(self):
        x = [0 for a in range(100)]
        for i in range(0,len(x)):
            x[i] = self.battery.read_u16()
            sleep_ms(2)
        dx = int(sum(x)/len(x))
        print(f"duty_16: {dx}.")
        if(dx < conf.BATTERY_MIN):
            return 0
        max_charge = conf.BATTERY_MAX-conf.BATTERY_MIN
        cur = dx - conf.BATTERY_MIN
        return round(100/max_charge*cur, 1)

###################################

def main():
    try:
        # Use the name of your method as a parameter when initialising the robot object. 
        r = Robot(True)
        #r.set_speed(100)
        while True:
            sleep(1)
            print(r.get_battery_charge())
    except KeyboardInterrupt:
        r.emergency_stop()
    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
