'''
The Swimbot code library
'''

import os
import sys
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


def wait_for_button_press():
    btn = Button()
    while True:
        if btn.any():
            return True
        else:
            return False


def calibrate_white(cl):
    debug_print("Calibrate Sensor...press button to exit")

    cl.mode = ColorSensor.MODE_COL_REFLECT

    btn = Button()
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

def Linefollow(s1,s2,color2follow,stop,var):
    rtmotor=motor(port.B)
    lfmotor=motor(port.C)
    cl1 = ColorSensor(s1)
    cl2 = ColorSensor(s2)
    cl1.mode = 'COL-REFLECT'
    cl2.mode = 'COL-REFLECT'
    move = True
    robot = DriveBase(lfmotor, rtmotr, WHEEL_DIAMETER, AXLE_TRACK)
    Drive()
    if stop = "rotations":
        while move=True:
            if lfmotor.degrees=Var:
                stop()
                break
            if cl1.reflected_light_intensity==-1,0,1:
                pass
            elif cl1.reflected_light_intensity>1 and cl2.reflected_light_intensity<-1:
                rtmotorturn(0-cl1.reflected_light_intensity)
            elif cl1.reflected_light_intensity<-1 and cl2.reflected_light_intensity>1:
                lfmotorturn(0-cl2.reflected_light_intensity)
    if stop = "color":
        while move=True:
            if var=Black
                if cl1.reflected_light_intensity<-40:
                    stop()
                    break
            if var=white
                if cl1.reflected_light_intensity>40:
                    stop()
                    break
            if var=gray
                if cl1.reflected_light_intensity==1,0,-1:
                    stop()
                    break
            if cl1.reflected_light_intensity==-1,0,1:
                pass
            elif cl1.reflected_light_intensity>1 and cl2.reflected_light_intensity<-1:
                rtmotorturn(0-cl1.reflected_light_intensity)
            elif cl1.reflected_light_intensity<-1 and cl2.reflected_light_intensity>1:
                lfmotorturn(0-cl2.reflected_light_intensity)
