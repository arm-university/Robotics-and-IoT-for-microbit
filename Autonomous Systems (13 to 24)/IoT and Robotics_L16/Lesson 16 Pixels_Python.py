from microbit import *
import neopixel
from random import randint

np = neopixel.NeoPixel(pin13, 12)
bright = 40

while True:
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (bright,0,0)
    np.show()
    sleep(1000)
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (0,bright,0)
    np.show()
    sleep(1000)
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (0,0,bright)
    np.show()
    sleep(1000)
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (bright,bright,bright)
    np.show()
    sleep(1000)