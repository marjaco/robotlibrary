# Documentation for crawly_joint.py 

## main 
Executed, this sets all servos to 90°.

## __init__ 
Initialize a joint in the Crawly robot. 
Explanation of parameters: 
j_type: Short for joint_type. Can be conf.SHOULDER_FRONT, conf.SHOULDER_REAR,
    conf.KNEE
name: The name of the joint. Use something useful like "front_right". 
left_side: True or False. Servo motors on the left side need to be inverted in the code. 
inverted: There are servo motors that turn in a different direction than other. In this case, set to True.
pin: The pin number that controls the servo motor. 

## up_step 
Move the lower thigh up by increment until the minimum angle is reached.
        

## down_step 
Move the lower thigh down by increment until the maximum angle is reached.
        

## forward_step 
This moves the leg forward by increment.

## backward_step 
This moves the leg backward by increment.

## park 
Park the leg e.g. stretch it. 

## curl 
Curl the leg e.g. go to smallest position.

## tap 
If this joint is a knee, it is tapped three times.

## calibrate 
Set all angles to 90°, so the legs can be attached correctly.  The joints are first moved to 0°, so ist can be
checked, that they can move.

