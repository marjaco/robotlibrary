from struct import pack, unpack


def decode_motor(msg: bytes):
    directions, left_speed, right_speed = unpack("<BBB", msg)
    return directions & 0x01, (directions & 0x02) >> 1, left_speed, right_speed


def encode_motor(left_forward, right_forward, left_speed, right_speed):
    directions = 0
    if left_forward:
        directions |= 0x01
    if right_forward:
        directions |= 0x02
    return pack("<BBB", directions, left_speed, right_speed)
