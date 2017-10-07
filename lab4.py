import time
import RPi.GPIO as  GPIO


# Sets the the pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# If the Pi has more than one script/circuit on the GPIO, warnings will print out.
# This turns off those warnings.
GPIO.setwarnings(False)


# Strings for printing out the actions performed by the robot
forward = 'Moving Forward...'
backward = 'Moving Backward...'
left = 'Moving Left...'
right = 'Moving Right...'
stopping = 'Stopping...'



# Functions to carry out movement of the robot
def moveForward():
        print(forward)
def stop():
        print(stopping)
def moveBackward():
        print(backward)
def moveLeft():
        print(left)
def moveRight():
        print(right)




moveForward()