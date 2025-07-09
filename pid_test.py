# Version 1.91
import time, random
import matplotlib.pyplot as plt
from datetime import datetime
def pid_controller(setpoint, pv, kp, ki, kd, previous_error, integral, dt):
    error = setpoint - pv
    integral += error * dt
    derivative = (error - previous_error) / dt
    control = kp * error + ki * integral + kd * derivative
    return control, error, integral


def main():
    setpoint = 0  # Desired setpoint
    pv = 0  # Initial process variable
    kp = 0.6  # Proportional gain
    ki = 0.5  # Integral gain
    kd = 0.1  # Derivative gain
    previous_error = -9
    integral = 0
    dt = 0.1  # Time step
    time_steps = []
    pv_values = []
    control_values = []
    setpoint_values = []
    # setpoint = 100
    print(str(int(time.time())))
    for i in range(200):  # Simulate for 100 time steps
            control, error, integral = pid_controller(setpoint, pv, kp, ki, kd, previous_error, integral, dt)
            print(f"Control: {control}")
            # print(f"Error: {error}")
            # print(f"Integral: {integral}")
            pv += control * dt
            # Update process variable based on control output (simplified)
            previous_error = error
            
            time_steps.append(i * dt)
            pv_values.append(pv)
            control_values.append(control)
            setpoint_values.append(setpoint)
            # if random.randint(0,100) >95:
            #    pv = random.randint(0,200)
            time.sleep(dt)


    print(datetime.now())

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time_steps, pv_values, label='Process Variable (PV)')
    plt.plot(time_steps, setpoint_values, label='Setpoint', linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Value')
    plt.title('Process Variable vs. Setpoint')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(time_steps, control_values, label='Control Output')
    plt.xlabel('Time (s)')
    plt.ylabel('Control Output')
    plt.title('Control Output over Time')
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    main()


