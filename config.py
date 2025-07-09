# Version 1.91
########## Configuration for the motors.
'''This defines the parameters for the motors. 

MAX_DUTY: Set to lower than the maximum not to overload the motors. Absolute maximum is 65535.
MIN_DUTY: Set this to the minimum duty cycle that the motor needs to start moving. 
MIN_SPEED: Only 0 is making sense here but if you want you can change that. Must be above 0 though. You set set this to a higher appropriate value.
MAX_SPEED: If you want another scale than 0-100, set the maximum here.

DEBOUNCE_WAIT: This defines the waiting time for the debouncing of the buttons. Leave as it is if 
you don't know what it means.

WHITE_DETECTED: Use these constants to check for white or black with the IR-sensor. Don't change!
BLACK_DETECTED: Use these constants to check for white or black with the IR-sensor. Don't change!

Motors and ultrasonic sensor must use consecutive pins. so, f. ex. the left motor uses pins 12 and 13. Use >None< if you don't use the device.
MLF and LRF are for four wheel drive.
ML: pin number for left motor (or left rear motor for four wheel drive).
MR: pin number for right motor (or right rear motor for four wheel drive).
MLF: pin number for left motor (or left front motor for four wheel drive). Use None if not used. 
MRF: pin number for right motor (or right front motor for four wheel drive). Use None if not used. 
US: pin number for the ultrasonic sensor. Use None if not used. 
IR: pin number for the infrared sensor. Use None if not used. 
SERVO: pin number for the servo motor. Use None if not used.

JS_X_MEDIAN 
JS_Y_MEDIAN
JS_MAX_DUTY
JS_MIN_DUTY: These define the parameters for the joystick. You need to calibrate the numbers. Look at joystick.py for details.
X_PIN = 26 Pin for the x direction in the joystick.
Y_PIN = 27 Pin for the y direction in the joystick. 
B_PIN = 0 Pin for the button in the joystick. 
ROBOT_NAME: You need to set a custom name if you use a remote control.

SERVO_MIN_DUTY: Only change if the servo doesn't move the required 180°.
SERVO_MAX_DUTY: Only change if the servo doesn't move the required 180°.
'''

MAX_DUTY = 60000 # Maximum duty for the motors. Absolute maximum is 65535.
MIN_DUTY = 0 # Minimum duty for the motors. Absolute minimum is 0.
MIN_SPEED = 0 # <-- Set this
MAX_SPEED = 100

########## Waiting time in milliseconds for any debouncing of buttons. 
DEBOUNCE_WAIT = 30

########## Configuration for the detecting black or white with the IR-sensor.
WHITE_DETECTED = 0
BLACK_DETECTED = 1

########## Configuration of pins
ML=12
MR=14
MLF=None #10
MRF=None #20
US=None #16
IR=None #11
SERVO=None #9

########## Configuration for the Joystick remote control
JS_X_MEDIAN = 29940 
JS_Y_MEDIAN = 30510
JS_MAX_DUTY = 65535
JS_MIN_DUTY = 260

X_PIN = 26
Y_PIN = 27
B_PIN = 0

########## Configuration of the name of the robot for matching with the remote control.
ROBOT_NAME = "HAL9000"

########## Configuration for the Servo in the robot
# If you mix different servo types with different duty cycles, you can use the type2 constant for this.
SERVO_MIN_DUTY = 1350 # Change only if the servo doesn't move 180°.
SERVO_MAX_DUTY = 8100 # Change only if the servo doesn't move 180°.
#SERVO_MIN_DUTY_TYPE2 = 1800 # In case you use different types of servos with different duty_cycles.
#SERVO_MAX_DUTY_TYPE2 = 7600 # In case you use different types of servos with different duty_cycles.