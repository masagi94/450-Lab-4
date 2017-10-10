import time                                                                              
import RPi.GPIO as  GPIO                                                                 
                                                                                         
        
 
#Functions to carry out movement of the robot                                            
# 0 = GPIO.LOW  1 = GPIO.HIGH                                                            
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
                                                                                         
                                                                                         
# Sets the desired pin numbering system to BCM                                           
GPIO.setmode(GPIO.BCM)                                                                   
                                                                                         
# Disables warnings in case the RPI.GPIO detects that a pin has been configured          
# to something other than the default (input)                                            
GPIO.setwarnings(False)                                                                  
                                                                                         
# These are the pins we will be using.                                                   
# 6 and 26 are ena and enb                                                               
# 12, 13, 20, 21 are IN1 IN2 IN3 IN4                                                     
chan_list = [6,12,13,20,21,26]                                                           
                                                                                         
# Sets all the pins stated above as outputs                                              
GPIO.setup(chan_list,GPIO.OUT)                                                           
                                                                                         
# creates objects "p1" and "p2", sets ena and enb to 50 Hz, starts them at 20% duty cycle
p1 = GPIO.PWM(6,50)                                                                      
p1.start(20)                                                                             
                                                                                         
p2 = GPIO.PWM(26,50)                                                                     
p2.start(20)
                                                                               
# Forward and backward movement                                                
# Used the sleep() function from the time library to create a delay in seconds 
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
                                                                               
# Pivots to the right by 90%.                                                  
# Movement to the right and back to the center                                 
pivotRight()                                                                   
time.sleep(.7) # .7 seconds = about 90%                                        
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
                                                                               
                                                                               
# Pivots to the left by 180%                                                   
# Movement to the left and back to the center                                  
pivotLeft()                                
time.sleep(1.25) # 1.25 second = about 180%
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
                                           
# Pivots to the right by 90%               
# Ends movement                            
pivotRight()                               
time.sleep(.7) # .7 seconds = about 90%    
stop()                                     
                                           
# Stops both the PWM outputs               
p1.stop()                                  
p2.stop()                                  
                                           
                                           
                                           
# Cleans up the used resources             
GPIO.cleanup()