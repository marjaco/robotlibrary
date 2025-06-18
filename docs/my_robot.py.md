# Documentation for my_robot.py 

## rc_button_pressed 
If the button on the rc is pressed, this function is called.

## ir_detected 
If the ir sensor detects something, this function is called.
pin.value() == 0: White detected (there is a reflection)
pin.value() == 1: Black detected (there is no reflection)

