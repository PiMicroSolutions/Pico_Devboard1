import machine
import time

led = machine.Pin(17, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)
