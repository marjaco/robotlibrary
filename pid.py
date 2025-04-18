import time, random
from robotlibrary.ir_array import IR_Array


class PID:
    def __init__(self,ir_array,dt):
        self.ir_array = ir_array
        self.setpoint = 0  # Desired setpoint
        self.pv = 0  # Initial process variable
        self.kp = 1.0  # Proportional gain
        self.ki = 0.1  # Integral gain
        self.kd = 0.05  # Derivative gain
        self.previous_error = 0
        self.integral = 0
        self.last_controlled_state_time = int(time.time_ns())
        self.dt = dt
          
                
    def pid_controller(self):
        error = self.ir_array.get_error()
        if error == 0:
            self.last_controlled_state_time = int(time.time_ns())
        #print(f"Error: {error}")
        self.integral += error * self.dt
        derivative = (error - self.previous_error) / self.dt
        self.previous_error = error
        control = self.kp * error + self.ki * self.integral + self.kd * derivative
        return control


def main():
    pid = PID(IR_Array(0,5),0.01)
    time.sleep_ms(10)
    while True:
        print(str(pid.pid_controller()))
        time.sleep_ms(10)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()


