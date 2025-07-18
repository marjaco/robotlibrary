# Documentation for config_crawly.py 

## Module 
These parameters define the Crawly robot.
SERVO_MIN_DUTY: Change only if the servo doesn't move 180°.
SERVO_MAX_DUTY: Change only if the servo doesn't move 180°.
SERVO_MIN_DUTY_TYPE2: In case you use different types of servos with different duty_cycles. You need to change the source code in crawly_joint.py
SERVO_MAX_DUTY_TYPE2: In case you use different types of servos with different duty_cycles. You need to change the source code in crawly_joint.py

These define the maximal movmeent parameters for the limbs:
SHOULDER_FRONT_MIN_ANGLE: backward motion
SHOULDER_FRONT_MAX_ANGLE: forward motion
SHOULDER_REAR_MIN_ANGLE: backward motion
SHOULDER_REAR_MAX_ANGLE: forward motion
KNEE_MIN_ANGLE: up motion
KNEE_MAX_ANGLE: down motion

US: Pin number for the ultrasonic sensor. 

Those parameters define the sensible angles for the movements of the robot:
CRAWLY_FRONT_FORWARD_ANGLE = 130
CRAWLY_FRONT_BACKWARD_ANGLE = 90
CRAWLY_REAR_FORWARD_ANGLE = 90
CRAWLY_REAR_BACKWARD_ANGLE = 50
CRAWLY_UP_ANGLE = 75
CRAWLY_DOWN_ANGLE = 90

Type of joint definitions:
SHOULDER_FRONT = 4
SHOULDER_REAR = 6
KNEE = 8

