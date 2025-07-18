# Documentation for config.py 

## Module 
This defines the parameters for the motors. 

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

JS_X_MEDIAN: These define the parameters for the joystick. You need to calibrate the numbers. Look at joystick.py for details.
JS_Y_MEDIAN: These define the parameters for the joystick. You need to calibrate the numbers. Look at joystick.py for details.
JS_MAX_DUTY
JS_MIN_DUTY

X_PIN = 26 Pin for the x direction in the joystick.
Y_PIN = 27 Pin for the y direction in the joystick. 
B_PIN = 0 Pin for the button in the joystick.

ROBOT_NAME: You need to set a custom name if you use a remote control.

SERVO_MIN_DUTY: Only change if the servo doesn't move the required 180°.
SERVO_MAX_DUTY: Only change if the servo doesn't move the required 180°.

