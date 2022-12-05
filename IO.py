import Jetson.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT,initial=GPIO.LOW)

GPIO.output(37,GPIO.HIGH)
time.sleep(1)

GPIO.output(37,GPIO.LOW)

time.sleep(1)


GPIO.output(37,GPIO.HIGH)
time.sleep(1)
GPIO.output(37,GPIO.LOW)
GPIO.cleanup()
