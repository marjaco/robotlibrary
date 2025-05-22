# Documentation for robotlibrary/crawly.py 

## Crawly 
This is the central class which manages and uses all the other components of the robot. The parameters are defined in config_crawly.py

## main 
Starting this file calibrates all servos and then terminates.

## reset_movement 
This needs to be called before each new movement of a leg. 

## move_forward 
This makes the crawler move forward in a coordinated way. Most of the functionality lies in the other classes Joint and Leg.
This method showcases a possible solution.

## move_backward 
This makes the crawler move backward in a coordinated way. Most of the functionality lies in the other classes Joint and Leg

## turn_left 
This makes the crawler turn to the left in one place in a coordinated way. Most of the funktionality lies in the other classes Joint and Leg

## turn_right 
This makes the crawler turn to the right in one place in a coordinated way. Most of the funktionality lies in the other classes Joint and Leg

## move_left 
This makes the crawler move to the left in a coordinated way. Most of the functionality lies in the other classes Joint and Leg.

## move_right 
This makes the crawler move to the right in a coordinated way. Most of the functionality lies in the other classes Joint and Leg.

## park 
This stretches legs the legs lengthwise, so the robot lies on its underside.

## curl 
This movement bends the legs, so the robot stands on tiptoes.

## calibrate 
This sets all servos to 90° so the legs can be assembled with the correct angles.

## tap 
This taps all the legs. Looks and sounds scary and can also identify the legs.

