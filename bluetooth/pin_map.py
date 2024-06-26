from machine import Pin
from micropython import const


MOTOR_LEFT_FORWARD = const(12)
MOTOR_LEFT_BACKWARD = const(13)
MOTOR_RIGHT_FORWARD = const(14)
MOTOR_RIGHT_BACKWARD = const(15)

pin_map = {
    MOTOR_LEFT_FORWARD: Pin(MOTOR_LEFT_FORWARD),
    MOTOR_LEFT_BACKWARD: Pin(MOTOR_LEFT_BACKWARD),
    MOTOR_RIGHT_FORWARD: Pin(MOTOR_RIGHT_FORWARD),
    MOTOR_RIGHT_BACKWARD: Pin(MOTOR_RIGHT_BACKWARD)
}
