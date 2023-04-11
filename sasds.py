import RPi.RPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

for i in range(10):
    GPIO.output(3,True)
    print("led is on")
    time.sleep(1)

    GPIO.output(3,True)
    print("led is off")
    time.sleep(1)

print("program complete")

    
