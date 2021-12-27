from machine import Pin
import time

led = Pin(16, Pin.OUT)

while True:
    led(1)
    time.sleep(1)
    led(0)
    time.sleep(1)