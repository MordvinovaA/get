import RPi.GPIO as gpio
from time import sleep
dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def decimal2binary(a):
    return [int (bit) for bit in bin(a)[2:].zfill(8)]
try:
    while (True):
        a=input('¬ведите период треугольного сигнала')
        if a=='q':
            break
        if not a.isdigit():
            print('¬ведено не целое число')
            continue
        b=int(a)/256/2
        for i in range(256):
            gpio.output(dac, decimal2binary(i))
            sleep(b)
        for i in range(255, -1, -1):
            gpio.output(dac, decimal2binary(i))
            sleep(b)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
  