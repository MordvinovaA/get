import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
leds=[21, 20, 16, 12, 7, 8, 25, 24]
comp=4
troyka=17
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def decimal2binary(a):
    return [int (bit) for bit in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, decimal2binary(k))
        sleep(0.07)
        if gpio.input(comp)==0:
            k-=2**i
    return k

def vol(a):
    a1=int(a/256*10)
    l=[0]*8
    for i in range(a1):
        l[i]=1
    return l

try:
    while True:
        a=adc()
        if a!=0:
            print(a, '{:.2f}v'.format(3.3*a/256))
        gpio.output(leds, vol(a))

        
finally:
    gpio.output(dac, 0)
    gpio.cleanup() 