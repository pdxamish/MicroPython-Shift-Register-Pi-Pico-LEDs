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

# Set the initial value of the shift register
value = 0b01010101    #alternates the on and off
#value = 0b0000000  for all on and off

while True:
    # Update the shift register with the current value
    update_shift_register(value)

    # Wait for a short time
    time.sleep(0.5)

    # Toggle the value of the shift register
    value = ~value & 0b11111111
