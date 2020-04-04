#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# controlGpio.py

import sys
import time
try:
    import gpiozero
    import RPi.GPIO as GPIO
except:
    print("Failed to import gpiozero/RPi.GPIO library")

# class Gpio:
#     def __init__(self, channel, inOut, name, state):
#         self.channel = channel # BCM channel numero
#         self.name = name # Name/function of the GPIO
#         self.state = state # Initial state of the GPIO
#         # TODO: init hardware
#         #self.gpio = gpiozero.LED(channel)
#         self.gpio = GPIO.setup(channel, inOut, initial=state)
#     def setState(state):
#         # TODO
#         self.state = state
#     def getState():
#         # TODO
#         return self.state

# BCM numbering
# Ev1 = 22
# Ev2 = 23
# Ev3 = 24
# Ev4 = 25
# Pump = 27

# Using RPi.GPIO library
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#channels = [22, 23, 24, 25, 27]
#GPIO.setup(channels, GPIO.OUT, initial=GPIO.LOW)
#states = (GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)
#GPIO.output(channels, states) # State can be 0=GPIO.LOW=False or 1=GPIO.HIGH=True
#GPIO.cleanup(channels)

gpios = [gpiozero.LED(22), gpiozero.LED(23), gpiozero.LED(24), \
gpiozero.LED(25), gpiozero.LED(27)]

def setPinState(index, state=0):
    """Set the state (on/off) of a GPIO pin and return the current value"""
    global gpios
    val = -1
    try:
        if state == 0:
            gpios[index].off()
        else:
            gpios[index].on()
        val = gpios[index].value
        print("Pin idx {}: requested state={}, value={}".format(index, state, val))
    except:
        print("Failed to set pin idx {} to state {}".format(index, state))
    
    return val

def getPinState(index):
    """Return the current state/value of the GPIO pin"""
    global gpios
    try:
        return gpios[index].value
    except:
        return -1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments: you must provide the pin index to test")
        exit(-1)
    index = int(sys.argv[1])
    for i in range(5):
        val = setPinState(index, 0)
        time.sleep(1.0)
        val = setPinState(index, 1)
        time.sleep(1.0)
