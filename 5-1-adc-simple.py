import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
troyka=17
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def decimal2binary(a):
    return [int (bit) for bit in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        b=decimal2binary(i)
        gpio.output(dac, b)
        c=gpio.input(comp)
        sleep(0.07)
        if c==0:
            return i

try:
    while True:
        a=adc()
        if a!=0:
            print(a, '{:.2f}v'.format(3.3*a/256))
        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()   
