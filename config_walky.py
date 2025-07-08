# Version 1.90
########## Configuration for the Servos in the Walky robot
# If you mix different servo types with different duty cycles, you can use the type2 constant for this.
SERVO_MIN_DUTY = 1350 # Change only if the servo doesn't move 180°.
SERVO_MAX_DUTY = 8100 # Change only if the servo doesn't move 180°.
SERVO_MIN_DUTY_TYPE2 = 1800 # In case you use different types of servos with different duty_cycles. You need to change the source code in walky_joint.py
SERVO_MAX_DUTY_TYPE2 = 7600 # In case you use different types of servos with different duty_cycles. You need to change the source code in walky_joint.py

########## Configuration for the Servos in the Walky robot
SHOULDER_FRONT_MIN_ANGLE =  45 # backward motion
SHOULDER_FRONT_MAX_ANGLE = 180 # forward motion
SHOULDER_REAR_MIN_ANGLE =  20 # backward motion
SHOULDER_REAR_MAX_ANGLE = 140 # forward motion
KNEE_MIN_ANGLE = 65 # up motion
KNEE_MAX_ANGLE = 180 # down motion

########## Configuration of pins
US=None #16


### Type definitions
SHOULDER_FRONT = 4
SHOULDER_REAR = 6
KNEE = 8
HIP = 10

########## Configuration for the servos movements in the Walky robot
HIP_FORWARD_ANGLE = 110
HIP_BACKWARD_ANGLE = 80
KNEE_FORWARD_ANGLE = 180
KNEE_BACKWARD_ANGLE = 120