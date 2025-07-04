# $version
# If you mix different servo types with different duty cycles, you can use the type2 constant for this.
SERVO_MIN_DUTY = 1350 # Change only if the servo doesn't move 180°.
SERVO_MAX_DUTY = 8100 # Change only if the servo doesn't move 180°.
SERVO_MIN_DUTY_TYPE2 = 1800 # In case you use different types of servos with different duty_cycles. You need to change the source code in crawly_joint.py
SERVO_MAX_DUTY_TYPE2 = 7600 # In case you use different types of servos with different duty_cycles. You need to change the source code in crawly_joint.py

########## Configuration for the Servos in the Crawly robot
SHOULDER_FRONT_MIN_ANGLE =  45 # backward motion
SHOULDER_FRONT_MAX_ANGLE = 180 # forward motion
SHOULDER_REAR_MIN_ANGLE =  20 # backward motion
SHOULDER_REAR_MAX_ANGLE = 140 # forward motion
KNEE_MIN_ANGLE = 65 # up motion
KNEE_MAX_ANGLE = 180 # down motion

########## Configuration of pins
US=None #16

### Configuration for the movements of Crawly. 
CRAWLY_FRONT_FORWARD_ANGLE = 130
CRAWLY_FRONT_BACKWARD_ANGLE = 90
CRAWLY_REAR_FORWARD_ANGLE = 90
CRAWLY_REAR_BACKWARD_ANGLE = 50
CRAWLY_UP_ANGLE = 75
CRAWLY_DOWN_ANGLE = 90

# Configurations for side walking
# CRAWLY_SIDE_WALKING_FRONT_ANGLE = 150
# CRAWLY_SIDE_WALKING_REAR_ANGLE = 30
# CRAWLY_SIDE_WALKING_CENTER_ANGLE = 90
# 
# CRAWLY_SIDE_WALKING_UP_ANGLE = 140
# CRAWLY_SIDE_WALKING_DOWN_ANGLE = 170


### Type definitions
SHOULDER_FRONT = 4
SHOULDER_REAR = 6
KNEE = 8