import os
import sys
import time
from time import sleep
from swimbotlib import *


def main():
    '''The main function of our program'''
    display_reset()

    # print something to the screen of the device
    print('Hello My World!')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code!')

    cl = ColorSensor()
    calibrate_white(cl)

    debug_print("Printing color...press button to exit")
    while True:
        debug_print(cl.color_name)
        sleep(0.05)

    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(5)


if __name__ == '__main__':
    main()
