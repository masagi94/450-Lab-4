import time
import RPi.GPIO as  GPIO



# Should we keep this function? Idk how much we're allowed to use from the provided code..
def __init__(self,in1=12,in2=13,ena=6,in3=20,in4=21,enb=26):
		self.IN1 = in1
		self.IN2 = in2
		self.IN3 = in3
		self.IN4 = in4
		self.ENA = ena
		self.ENB = enb

		# Sets the the pin numbering mode to BCM
		GPIO.setmode(GPIO.BCM)

		# If the Pi has more than one script/circuit on the GPIO, warnings will print out.
		# This turns off those warnings.
		GPIO.setwarnings(False)
		
		GPIO.setup(self.IN1,GPIO.OUT)
		GPIO.setup(self.IN2,GPIO.OUT)
		GPIO.setup(self.IN3,GPIO.OUT)
		GPIO.setup(self.IN4,GPIO.OUT)
		GPIO.setup(self.ENA,GPIO.OUT)
		GPIO.setup(self.ENB,GPIO.OUT)
		
		self.forward()
		
		self.PWMA = GPIO.PWM(self.ENA,500)
		self.PWMB = GPIO.PWM(self.ENB,500)
		self.PWMA.start(50)
		self.PWMB.start(50)

# Functions to carry out movement of the robot
# Can make funtion move robot by a set amount each time, or use parameters for desired amount
# 0 = GPIO.LOW	1 = GPIO.HIGH
def moveForward(time):
        print("Moving Forward...")
        GPIO.output(,1)
        GPIO.output(,0)
        GPIO.output(,0)
        GPIO.output(,1)

def stop(time):
        print("Stopping...")
        GPIO.output(,0)
        GPIO.output(,0)
        GPIO.output(,0)
        GPIO.output(,0)

def moveBackward(time):
        print("Moving Backward...")
        GPIO.output(,0)
        GPIO.output(,1)
        GPIO.output(,1)
        GPIO.output(,0)

def moveLeft(time):
        print("Moving Left...")
        GPIO.output(,0)
        GPIO.output(,0)
        GPIO.output(,0)
        GPIO.output(,1)

def moveRight(time):
        print("Moving Right...")
        GPIO.output(,1)
        GPIO.output(,0)
        GPIO.output(,0)
        GPIO.output(,0)





moveForward()