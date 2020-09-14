#!/usr/bin/env python3
'''
The Swimbot code library
'''

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.led import Leds

# state constants
ON = True
OFF = False

color_array = ['No color', 'Black', 'Blue',
               'Green', 'Yellow', 'Red', 'White', 'Brown']

def color(x):
    return color[x]

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


def initialize_leds():
    leds = Leds()
    leds.set_color('LEFT', 'AMBER')
    leds.set_color('RIGHT', 'YELLOW')


def press_button():
    btn = Button()
    while True:
        if btn.any():
            return True
        else:
            return False


def calibrate_white(cl):
    btn = Button()
    debug_print("Calibrate Sensor...press button to exit")
    cl.mode = ColorSensor.MODE_COL_REFLECT
    while True:
        if btn.any():
            return
        else:
            cl.calibrate_white()



def display_reset():
    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

