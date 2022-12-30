from machine import Pin, SPI
import time

# Initialize the shift register
data_pin = Pin(13, Pin.OUT)
clock_pin = Pin(14, Pin.OUT)
latch_pin = Pin(15, Pin.OUT)

# Create a function to update the shift register
def update_shift_register(value):
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

# Create a function to shift the LEDs left
def shift_left(value):
    return ((value << 1) & 0b11111111) | (value >> 5)

# Create a function to shift the LEDs right
def shift_right(value):
    return (value >> 1) | ((value << 5) & 0b11111111)

# Create a function to rotate the LEDs
def rotate(value):
    return (value >> 1) | ((value & 1) << 5)

# Set the initial value of the shift register
value = 0b00000001

while True:
    # Update the shift register with the current value
    update_shift_register(value)

    # Wait for a short time
    time.sleep(0.7)

    # Shift the LEDs left
    value = shift_right(value)
