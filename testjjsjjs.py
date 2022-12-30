from machine import Pin
import utime

led_blue = Pin(16, Pin.OUT)
led_green = Pin(18, Pin.OUT)
led_red = Pin(17, Pin.OUT)
#

led_blue.value(1)
