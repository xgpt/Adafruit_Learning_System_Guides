import board
import neopixel
import time

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
PURPLE = (10, 0, 25)
PINK = (25, 0, 10)

while True:
    pixel[0] = (PURPLE)
    time.sleep(0.5)
    pixel[0] = (PINK)
    time.sleep(0.5)
