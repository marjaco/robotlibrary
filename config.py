########## Configuration for the Joystick remote control

'''This defines the parameters for the joystick. Don't change if you don't know what you are doing.'''
JS_X_MEDIAN = 29940 
JS_Y_MEDIAN = 30510
JS_MAX_DUTY = 65535
JS_MIN_DUTY = 260

########## Configuration of the name of the robot for matching with the remote control.
ROBOT_NAME = "HAL9000"

########## Configuration for the motors.
'''This defines the parameters for the motors. 

MAX_DUTY: Set to lower than the maximum not to overload the motors.

MIN_DUTY: You can leave this at 0. Set MIN_SPEED instead.

MIN_SPEED: Set this to a value slightly below the speed that sets the robot in motion. 

MAX_SPEED: If you want another scale than 0-100, set the maximum here. '''
MAX_DUTY = 60000 # Maximum duty for the motors. Absolute maximum is 65535.
MIN_DUTY = 0 # Minimum duty for the motors. Absolute minimum is 0.
MIN_SPEED = 45
MAX_SPEED = 100

########## Waiting time in millliseconds for any debouncing of buttons. 
'''This defines the waiting time for the debouncing of the buttons. Leave as it is if 
you don't know what it means.'''
DEBOUNCE_WAIT = 30

########## Configuration for the detecting black or white with the IR-sensor.
'''Use these constants to check for white or black with the IR-sensor.'''
WHITE_DETECTED = 0
BLACK_DETECTED = 1

########## Configuration of pins
'''Motors and ultrasonic sensor must use consecutive pins. Use >None< if you don't use the sensor.'''
ML=12
MR=14
US=16
IR=None #11
SERVO=None #9


########## Configuration for the Servos in the Crawly robot

SERVO_MIN_DUTY = 1350
SERVO_MAX_DUTY = 8100
SHOULDER_FRONT_MIN_ANGLE =  45 # backward motion
SHOULDER_FRONT_MAX_ANGLE = 180#165 # forward motion
SHOULDER_REAR_MIN_ANGLE =  20 # backward motion
SHOULDER_REAR_MAX_ANGLE = 140#140 # forward motion
KNEE_MIN_ANGLE = 65 # up motion
KNEE_MAX_ANGLE = 180 # down motion

### Configuration for the movements of Crawly
CRAWLY_FRONT_FORWARD_ANGLE = 130
CRAWLY_FRONT_BACKWARD_ANGLE = 90
CRAWLY_REAR_FORWARD_ANGLE = 90
CRAWLY_REAR_BACKWARD_ANGLE = 50
CRAWLY_UP_ANGLE = 75
CRAWLY_DOWN_ANGLE = 90

### Type definitions

SHOULDER_FRONT = 4
SHOULDER_REAR = 6
KNEE = 8
HIP = 10

########## Configuration for the servos in the Walky robot


