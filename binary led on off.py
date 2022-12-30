from machine import Pin, SPI
import time

# Initialize the shift register
data_pin = Pin(13, Pin.OUT)
clock_pin = Pin(14, Pin.OUT)
latch_pin = Pin(15, Pin.OUT)

# Turn onn the first five output pins
value = 0b00000000
data_pin.value(1)
latch_pin.value(0)
for i in range(8):
    if value & (1 << i):
        data_pin.value(0)
    else:
        data_pin.value(1)
    clock_pin.value(0)
    clock_pin.value(1)
latch_pin.value(1)

# Wait for a short time
time.sleep(1)

# Turn off the first five output pins
value = 0b11111111
data_pin.value(1)
latch_pin.value(0)
for i in range(8):
    if value & (1 << i):
        data_pin.value(0)
    else:
        data_pin.value(1)
    clock_pin.value(0)
    clock_pin.value(1)
latch_pin.value(1)


