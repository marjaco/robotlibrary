# Version 2.0
import machine
import utime as time
from machine import Pin
import micropython
from robotlibrary.config import DEBOUNCE_WAIT
micropython.alloc_emergency_exception_buf(100)
class Rotary:
    '''This class deals with the rotary encoders for the remote control. Don't use directly or edit.'''
    ROT_CW = 1
    ROT_CCW = 2
    SW_PRESS = 4
    SW_RELEASE = 8
    
    def __init__(self,dt,clk,sw,rc):
        self.dt_pin = Pin(dt, Pin.IN, Pin.PULL_UP)
        self.clk_pin = Pin(clk, Pin.IN, Pin.PULL_UP)
        self.sw_pin = Pin(sw, Pin.IN, Pin.PULL_UP)
        self.rc = rc
        self.last_status = (self.dt_pin.value() << 1) | self.clk_pin.value()
        self.dt_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING )
        self.clk_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING )
        self.sw_pin.irq(handler=self.switch_detect, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING )
        self.last_button_status = self.sw_pin.value()
        self.last_change = time.ticks_ms()
        
    def rotary_change(self, pin):
        while time.ticks_diff(time.ticks_ms(), self.last_change) < DEBOUNCE_WAIT: 
            pass
        self.last_change = time.ticks_ms()
        new_status = (self.dt_pin.value() << 1) | self.clk_pin.value()
        if new_status == self.last_status:
            return
        transition = (self.last_status << 2) | new_status
        if transition == 0b1110:
            self.rc.rotary_changed(Rotary.ROT_CW)
        elif transition == 0b1101:
            self.rc.rotary_changed(Rotary.ROT_CCW)
        self.last_status = new_status
        
    def switch_detect(self,pin):
        if self.last_button_status == self.sw_pin.value():
            return
        self.last_button_status = self.sw_pin.value()
        if self.sw_pin.value():
            self.rc.button()
            
        

            
