from machine import Pin, SPI
import time

# Initialize the shift register
data_pin = Pin(13, Pin.OUT)
clock_pin = Pin(14, Pin.OUT)
latch_pin = Pin(15, Pin.OUT)

# Turn all the LEDs off

# Chase the LEDs
while True:
    data_pin.value(0)
    latch_pin.value(1)
    for _ in range(8):
        clock_pin.value(1)
        clock_pin.value(0)
    latch_pin.value(0)
    
    
    
    
    