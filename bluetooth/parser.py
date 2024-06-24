from struct import pack, unpack


def decode_motor(data: bytes):  # returns Tuple[bool, bool int, int] Does it?
    speed, turn, forward = unpack("<bbb", data)
    return speed, turn, forward==0
    #return bool(directions & 0x01), bool((directions & 0x02) >> 1), left_speed, right_speed


def encode_motor(speed: int, turn: int, forward: bool) -> bytes:
   return pack("<bbb", speed, turn, forward==0)


#print(decode_motor(encode_motor(50,30,False)))