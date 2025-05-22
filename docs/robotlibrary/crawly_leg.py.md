# Documentation for robotlibrary/crawly_leg.py 

## main 
This file, executed, taps the leg.

## reset_movement 
This needs to be called before the leg starts moving.

## forward_move_forward 
This makes a small adjustment in the move forward of this leg. Returns True as long as the movement is NOT finished
and returns False, once the movement is finished. This does not move the robot forward, 
as the leg is raised in this movement.

## forward_move_backward 
This makes a small adjustment in the move backward of this leg. Returns True as long as the movement is NOT finished
and returns False, once the movement is finished. This does actually move the robot forward, 
as the leg is lowered.

## backward_move_forward 
This makes a small adjustment in the move forward of this leg. Returns True as long as the movement is NOT finished
and returns False, once the movement is finished. This does not move the robot backward, 
as the leg is lowered.

## backward_move_backward 
This makes a small adjustment in the move backward of this leg. Returns True as long as the movement is NOT finished
and returns False, once the movement is finished. This does actually move the robot backward, 
as the leg is raised in this movement.

## left_move_ahead 
This makes the leg go to the very front or very back of the robot depended on the position of the shoulder.
The knee is raised or lowered depended on the side where it is mounted on.
This is used to move the robot to the left.

## left_move_center 
This makes the leg go to the center, which means setting the servo on 90 degrees.
The knee is raised or lowered depended on the side where it is mounted on.
This is used to move the robot to the left.

## right_move_ahead 
This makes the leg go to the very front or very back of the robot depended on the position of the shoulder.
The knee is raised or lowered depended on the side where it is mounted on.
This is used to move the robot to the right.

## right_move_center 
This makes the leg go to the center, which means setting the servo on 90 degrees.
The knee is raised or lowered depended on the side where it is mounted on.
This is used to move the robot to the right.

## park 
This streteches the leg.

## calibrate 
This sets all the servos to 90°

## curl 
This bends the knees and sets the shoulder to 90°.

## tap 
Taps the leg.

