from machine import Pin
import time

# Initialize the shift register pins
data_pin = Pin(13, Pin.OUT)
clock_pin = Pin(14, Pin.OUT)
latch_pin = Pin(15, Pin.OUT)

# Set the initial value of the shift register
value = 0b00000001

while True:
    # Set the value of the data pin
    data_pin.value(value & 0b10000000)

    # Toggle the clock pin
    clock_pin.value(0)
    clock_pin.value(1)
    data_pin.value(value & 0b01000000)
    clock_pin.value(0)
    clock_pin.value(1)
    data_pin.value(value & 0b00100000)
    clock_pin.value(0)
    clock_pin.value(1)
    data_pin.value(value & 0b00010000)
    clock_pin.value(0)
    clock_pin.value(1)
    data_pin.value(value & 0b00001000)
    clock_pin.value(0)
    clock_pin.value(1)
    data_pin.value(value & 0b00000100)
    clock_pin.value(0)
    clock_pin.value(1)
    data_pin.value(value & 0b00000010)
    clock_pin.value(0)
    clock_pin.value(1)
    data_pin.value(value & 0b00000001)
    clock_pin.value(0)
    clock_pin.value(1)

    # Toggle the latch pin
    latch_pin.value(0)
    latch_pin.value(1)

    # Wait for a short time
    time.sleep(0.1)

    # Toggle the value of the shift register
    value = value ^ 0b11111111
