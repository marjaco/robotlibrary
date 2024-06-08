from struct import pack, unpack


def decode_motor(data: bytes):  # returns Tuple[bool, bool int, int]
    directions, left_speed, right_speed = unpack("<BBB", data)
    return bool(directions & 0x01), bool((directions & 0x02) >> 1), left_speed, right_speed


def encode_motor(left_forward: bool, right_forward: bool, left_speed: int, right_speed: int) -> bytes:
    directions = 0
    if left_forward:
        directions |= 0x01
    if right_forward:
        directions |= 0x02
    return pack("<BBB", directions, left_speed, right_speed)
