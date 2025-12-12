import storage
import board
import digitalio
import time
import payload
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

pin = digitalio.DigitalInOut(board.GP10)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.DOWN   # Ensure a known state when nothing is connected

# The Pico's onboard LED is on pin GP25 / board.LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

if pin.value:
    led.value = True
    payload.payload()
            
else:
    led.value = False
    time.sleep(0.5)
