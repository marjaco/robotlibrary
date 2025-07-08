# Version 1.90
from machine import Pin
from time import sleep, sleep_ms
BLACK = 1

class IR_Array:
    def __init__(self, pin, count):
        #assert count % 2 != 0, "count must be uneven"
        self.pins = [0 for x in range(count)]
        self.error_values = [0 for x in range(count)]
        for i in range(count):
            self.pins[i] = Pin(pin+i, Pin.IN, Pin.PULL_UP)
        self.middle = count // 2
        self.error_values[self.middle] = 0
        for x in range(count // 2):
            if count % 2 == 1:
                self.error_values[self.middle+(x+1)] = (x+1)*3
            else:
                self.error_values[self.middle+(x)] = (x+1)*3
            self.error_values[self.middle-(x+1)] = -(x+1)*3

        #print(self.error_values)

    def _get_values(self):
        return [self.pins[i].value() for i in range(len(self.pins))]
        
    def get_error(self):
        sum = 0
        values = self._get_values()
        #print(values)
        for i in range(len(values)):
            sum += self.error_values[i] * values[i]
        return sum
            
def main(): 
    ir = IR_Array(0,5)
    while True:
        e = ir.get_error()
        if e == 0:
            print("on track")
        elif e < 0 :
            print("go right")
        else:
            print("go left")
        #print(f"Error: {ir.get_error()}")
        sleep_ms(1000)

        
if __name__ == "__main__":
    # execute only if run as a script
    main()
            