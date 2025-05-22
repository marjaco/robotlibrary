# Documentation for robotlibrary/crawly_joint.py 

## main 
Executed, this sets all servos to 90°.

## __init__ 
Initialize a joint in the Crawly robot. 
Explanation of parameters: 
j_type: Short for joint_type. Can be robotlibrary.config_crawly.SHOULDER_FRONT, robotlibrary.config_crawly.SHOULDER_REAR, 
    robotlibrary.config_crawly.KNEE
name: The name of the joint. Use something useful like "front_right". 
left_side: True or False. Servo motors on the left side need to be inverted in the code. 
inverted: There are servo motors that turn in a different direction than other. In this case, set to True.
pin: The pin number that controls the servo motor. 

## reset_movement 
This is called before each new leg movement cycle.

## up 
If this object is a knee, it is moved up in one go. As the movement is then finished, it 
returns False. 

## down 
If this object is a knee, it is moved down in one go. As the movement is then finished, it 
returns False. 

## up_smooth 
This is not yet a good solution. It still moves the leg up or down before
the shoulder joint is moved and makes for an awkward movement. It should be
integrated into the movement in a way that makes it rise or lower only as much
as needed before the shoulder is moved. But how?

## down_smooth 
This is not yet a good solution. It still moves the leg up or down before
the shoulder joint is moved and makes for an awkward movement. It should be
integrated into the movement in a way that makes it rise or lower only as much
as needed before the shoulder is moved. But how?

## up_smooth_v2 
UNTESTED version for smooth movement.
        

## down_smooth_v2 
UNTESTED version for smooth movement.
        

## forward 
See the documentation for crawly_leg.py for information.

## backward 
See the documentation for crawly_leg.py for information.

## side_walking_up 
If this object is a knee, it is moved slowly. As the movement is then finished, it 
returns False. 

## side_walking_down 
If this object is a knee, it is moved down slowly. As the movement is then finished, it 
returns False. 

## ahead 
See the documentation for crawly_leg.py for information.

## center 
See the documentation for crawly_leg.py for information.

## tap 
If this joint is a knee, it is tapped three times.

