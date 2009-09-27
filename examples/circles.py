#!/usr/bin/python

from pypixel import *

def circles():
    hue = 0
    size = 10
    while True:
        for x in xrange(0, WIDTH + 1, size):
            for y in xrange(0, HEIGHT + 1, size):
                circle(hsv((hue, 100, 100)), (x, y), size)
                hue += 1
                hue %= 360
            update()

run(circles)
