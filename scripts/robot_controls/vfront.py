import RPi.GPIO as GPIO
import re
import time

WORDS = ["move","front"]

def isValid(text):
    return bool(re.search(r'\bmove|front\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    
     
    GPIO.setmode(GPIO.BOARD)
     
    Motor1A = 16
    Motor1B = 18
    Motor1E = 22
     
    Motor2A = 23
    Motor2B = 21
    Motor2E = 19
     
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
     
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)

        if True:
            if (bool(re.search(r'\bmove|front\b', text, re.IGNORECASE))):
                  GPIO.output(Motor1A,GPIO.HIGH)
                  GPIO.output(Motor1B,GPIO.LOW)
                  GPIO.output(Motor1E,GPIO.HIGH)
     
                  GPIO.output(Motor2A,GPIO.HIGH)
                  GPIO.output(Motor2B,GPIO.LOW)
       	      GPIO.output(Motor2E,GPIO.HIGH)
     
                  sleep(2)
     
                  message = ["hello"]
                  mic.say(message)
            GPIO.cleanup()    
  

