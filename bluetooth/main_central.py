# Version 2.0.1
from time import sleep
from central import BLECentral
from ble_services_definitions import MOTOR_TX_UUID, MOTOR_RX_UUID, ROBOT_UUID
from parser import encode_motor, decode_motor


def read(buffer):
    left_direction, right_direction, left_speed, right_speed = decode_motor(bytes(buffer))
    print(f"set left motor forwards: {left_direction} with speed {left_speed}")
    print(f"set right motor forwards: {right_direction} with speed {right_speed}")


def main():
    server = BLECentral(True)
    server.register_read_callback(MOTOR_TX_UUID, read)

    server.scan()

    print("waiting for connection")
    while not server.is_connected():
        sleep(1)

    print("Found connection")

    while True:
        text = input("Please input in format: left_forward, right_forward, left_speed, right_speed: ")
        [left_forward, right_forward, left_speed, right_speed] = text.split(", ")
        left_forward, right_forward, left_speed, right_speed = (left_forward == "True", right_forward == "True",
                                                                int(left_speed), int(right_speed))
        print(left_forward, right_forward)
        data = encode_motor(left_forward, right_forward, left_speed, right_speed)
        server.send(ROBOT_UUID, MOTOR_RX_UUID, data)


if __name__ == "__main__":
    main()
