
class Steering:
    def __init__ (self, rc):
        self.rc = rc
        
    def parse_values(speed: int, turn: int, forward: bool, button:bool):
        if turn > 20 or turn < -20:
            speed = rc.speed
        if turn < 30 or turn > -30:
            
        return speed, turn, forward, button
    
    
