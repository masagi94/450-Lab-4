import time
import RPi.GPIO as  GPIO



# Should we keep this function? Idk how much we're allowed to use from the provided code..
# def __init__(self,in1=12,in2=13,ena=6,in3=20,in4=21,enb=26):
# 		self.IN1 = in1
# 		self.IN2 = in2
# 		self.IN3 = in3
# 		self.IN4 = in4
# 		self.ENA = ena
# 		self.ENB = enb

		# Sets the the pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# If the Pi has more than one script/circuit on the GPIO, warnings will print out.
# This turns off those warnings.
GPIO.setwarnings(False)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

#self.forward()
# ena
GPIO.PWM(6,500)
GPIO.PWM(6,500).start(50)

# enb
GPIO.PWM(26,500)
GPIO.PWM(26,500).start(50)

# self.PWMA = GPIO.PWM(self.ENA,500)
# self.PWMB = GPIO.PWM(self.ENB,500)
# self.PWMA.start(50)
# self.PWMB.start(50)

# Functions to carry out movement of the robot
# Can make funtion move robot by a set amount each time, or use parameters for desired amount
# 0 = GPIO.LOW	1 = GPIO.HIGH
def moveForward():
        print("Moving Forward...")
        GPIO.output(12,1)
        GPIO.output(13,0)
        GPIO.output(20,0)
        GPIO.output(21,1)

def stop():
        print("Stopping...")
        GPIO.output(12,0)
        GPIO.output(13,0)
        GPIO.output(20,0)
        GPIO.output(21,0)

def moveBackward():
        print("Moving Backward...")
        GPIO.output(12,0)
        GPIO.output(13,1)
        GPIO.output(20,1)
        GPIO.output(21,0)

def moveLeft():
        print("Moving Left...")
        GPIO.output(12,0)
        GPIO.output(13,0)
        GPIO.output(20,0)
        GPIO.output(21,1)

def moveRight():
        print("Moving Right...")
        GPIO.output(12,1)
        GPIO.output(13,0)
        GPIO.output(20,0)
        GPIO.output(21,0)

def pivotRight():
		print("Right Pivot...")
        GPIO.output(12,1)
        GPIO.output(13,0)
        GPIO.output(20,1)
        GPIO.output(21,0)

def pivotLeft():
		print("Left Pivot...")
        GPIO.output(12,0)
        GPIO.output(13,1)
        GPIO.output(20,0)
        GPIO.output(21,1)


# Forward and backward movement
moveForward()
time.sleep(5)
stop()
time.sleep(1)
moveBackward()
time.sleep(10)
stop()
time.sleep(1)
moveForward()
time.sleep(5)
stop()
time.sleep(1)

# Movement to the right and back to the center
# He wants a pivot, not a turn left or turn right. Made a function for that, dont know if it works
pivotRight()
time.sleep(1) # How much time would be needed to pivot 90%?
stop()
time.sleep(1)
moveForward()
time.sleep(5)
stop()
time.sleep(1)
moveBackward()
time.sleep(5)
stop()
time.sleep(1)


# Movement to the left and back to the center
pivotLeft()
time.sleep(2) # Again, how much time would pivoting take?
stop()
moveForward()
time.sleep(5)
stop()
time.sleep(1)
moveBackward()
time.sleep(5)
stop()
time.sleep(1)

# Face forward, ends movement.
pivotRight()
time.sleep(1)
stop()




# Cleans up the used resources
GPIO.cleanup()