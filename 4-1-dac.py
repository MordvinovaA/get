import RPi.GPIO as gpio
import sys
dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def decimal2binary(a):
    return [int (bit) for bit in bin(a)[2:].zfill(8)]
try:
    while (True):
        a=input('������� ����� ����� �� 0 �� 255')
        if a=='q':
            sys.exit()
        elif  a.isdigit() and 0<=int(a)<=255:
            gpio.output(dac, perev(int(a), 8))
            print("{:.4f}".format(int(a)/256*3.3))
        elif not a.isdigit():
            try:
                if int(a)<0:
                    print('������� ������������� �����')
            except(ValueError):
                print('������� �� �����')
        elif int(a)<0 or int(a)>255:
            print('�������� ��� ���������')         
except ValueError:
    print('������� �� �����')
except KeyboardInterrupt:
    print('done')
finally:
    gpio.output(dac, 0)
    gpio.cleanup()