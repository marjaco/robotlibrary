from machine import PWM, Pin
from pin_map import pin_map


class Motor:
    def __init__(self, gpio_pin_forwards: int, gpio_pin_backwards: int, on_change_callback=None):  # callable(bool, int)
        self.MAX_SPEED = 58000  # The absolute maximum is: 65535.
        self._callback = on_change_callback

        if gpio_pin_forwards in pin_map:
            self._current_pwm = PWM(pin_map[gpio_pin_forwards])
        else:
            self._current_pwm = PWM(Pin(gpio_pin_backwards))

        if gpio_pin_backwards in pin_map:
            self._paused_pwm = PWM(pin_map[gpio_pin_backwards])
        else:
            self._paused_pwm = PWM(Pin(gpio_pin_backwards))

        self._speed = 0
        self._moving_forwards = True
        self._current_pwm.freq(50000)
        self._paused_pwm.freq(50000)
        self._current_pwm.duty_u16(0)
        self._paused_pwm.duty_u16(0)

    def get_speed(self) -> int:
        return int((self._speed / self.MAX_SPEED) * 255)

    def set_speed(self, speed: int):
        if not 0 <= speed <= 255:
            raise ValueError(f"Invalid speed {speed} set. Range is 0 - 255")
        self._speed = int(self.MAX_SPEED * (speed / 255))
        self._current_pwm.duty_u16(self._speed)

        if self._callback is not None:
            self._callback(self._moving_forwards, self.get_speed())

    def set_direction(self, forwards: bool):
        if self._moving_forwards == forwards:
            return
        self._current_pwm.duty_u16(0)
        self._current_pwm, self._paused_pwm = self._paused_pwm, self._current_pwm
        self._current_pwm.duty_u16(self._speed)
        self._moving_forwards = forwards

        if self._callback is not None:
            self._callback(self._moving_forwards, self.get_speed())

    def moving_forwards(self) -> bool:
        return self._moving_forwards
