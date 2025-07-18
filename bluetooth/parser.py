# Version 1.92
from struct import pack, unpack


def decode_motor(data: bytes):  # returns Tuple[bool, bool int, int] Does it?
    speed, turn, forward, button_press = unpack("<bbbb", data)
    return speed, turn, forward==0, button_press==1

def encode_motor(speed: int, turn: int, forward: bool, button_press: bool) -> bytes:
   return pack("<bbbb", speed, turn, forward==0, button_press==1)
