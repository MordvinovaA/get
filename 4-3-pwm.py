import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.OUT)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT)
p=gpio.PWM(24, 1000)
p.start(0)

try:
        while True:
                d=int(input())
                p.ChangeDutyCycle(d)
                print("{:.4f}".format(d*3.3/100))
finally:
        gpio.output(24, 0)
        gpio.output(dac, 0)
        gpio.cleanup()        
        
       