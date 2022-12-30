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
value = 0

while True:
    # Update the shift register with the current value
    update_shift_register(value)

    # Wait for a short time
    time.sleep(1)

    # Increment the value of the shift register
    value += 1
    if value > 0b11111111:
        # Reset the value of the shift register
        value = 0
    elif value > 0b01111111:
        # Keep the last two LEDs on
        value = 0b01111111
    elif value > 0b00111111:
        # Keep the last three LEDs on
        value = 0b00111111
