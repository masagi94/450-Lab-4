import RPi.GPIO as  GPIO
import time

servo1 = 22 # azimuth, side to side
servo2 = 27 # elevation, up and down

angle1 = 0 # starting angle for servo1
angle2 = 0 # starting angle for servo2
dualAngle = 0 # used for changing both the servo angles

# Sets the desired pin numbering system to BCM
GPIO.setmode(GPIO.BCM)

# Disables warnings in case the RPI.GPIO detects that a pin has been configured
# to something other than the default (input)
GPIO.setwarnings(False)

# These are the pins we will be using.
chan_list = [servo1,servo2]

# Sets the pins stated above as inputs
GPIO.setup(chan_list,GPIO.OUT)



### Function for changing the duty cycle
# Only changes servo 1
def Servo1Angle(angle):
        p1.ChangeDutyCycle(2.5 + 10.0*angle/180)

# Only changes servo 2
def Servo2Angle(angle):
        p2.ChangeDutyCycle(2.5 + 10.0*angle/180)

# Changes both servos at the same time
def DualServoAngle(angle):
        p1.ChangeDutyCycle(2.5 + 10.0*angle/180)
        p2.ChangeDutyCycle(2.5 + 10.0*angle/180)



# Creates objects "p1" and "p2", sets frequency to 50 Hz, starts at 5% duty cycle
p1 = GPIO.PWM(servo1,50)
p2 = GPIO.PWM(servo2,50)
p1.start(5)
p2.start(5)
time.sleep(.25)

# Loop and adjust servos until break hit
while True:

        # Adjusts the first servo, increments of 5%
        if (angle1 < 180):
                angle1 += 5
                Servo1Angle(angle1)
                print("Servo 1 angle changed to %d...") % angle1
                time.sleep(.25)

        # Resets the servo to 5% in one step, then sets to 90% for servo 2 to have room to move
        elif (angle1 == 180):
                Servo1Angle(5)
                print("Servo 1 reset...")
                time.sleep(2)
                Servo1Angle(90)
                print("Servo 1 set to 90...")
                time.sleep(.5)
                angle1 += 5

        # Adjusts the second servo, increments of 5%
        elif (angle2 < 180):
                angle2 += 5
                Servo2Angle(angle2)
                print("Servo 2 angle changed to %d...") % angle2
                time.sleep(.25)

        # Resets the servo back to 5% in one step
        elif (angle2 == 180):
                Servo2Angle(5)
                print("Servo 2 reset...")
                time.sleep(2)
                angle2 += 5

        # Adjusts both the servos, increments of 10%
        elif (dualAngle < 180):
                dualAngle += 10
                DualServoAngle(dualAngle)
                print("Both servo angle's changed to %d...") % dualAngle
                time.sleep(.25)

        # Resets both servos back to 10%
        elif (dualAngle == 180):
                DualServoAngle(10)
                print("Both servos reset...")
                time.sleep(2)
                break           # Breaks out of code when done



# Cleans up resources
p1.stop()
p2.stop()
GPIO.cleanup()

















