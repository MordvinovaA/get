import RPi.GPIO as gpio
import time
from matplotlib import pyplot

gpio.setmode(gpio.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24] 
gpio.setup(leds, gpio.OUT)

dac = [26, 19, 13, 6, 5, 11, 9, 10] 
gpio.setup(dac, gpio.OUT, initial = gpio.HIGH)
comp = 4 
troyka =  17 

gpio.setup(comp, gpio.IN)

#Двоичное представление числа
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

#Получение напряжения на выходе тройка-модуля
def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        gpio.output(dac, decimal2binary(k))
        time.sleep(0.005)
        if gpio.input(comp) == 0:
            k -= 2**i
    return(k)

try:
    data = []
    voltage = 0
    start_time = time.time()
    c = 0

    #Подача 3.3 В на вход тройка-модуля
    gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)

    #Проведение измерений во время заряда конденсатора
    print('Зарядка конденсатора')
    while voltage < 256*0.9:
        voltage = adc()
        data.append(voltage)
        time.sleep(0.005)
        c += 1
        gpio.output(leds, decimal2binary(voltage))

    #Подача 0.0 В на вход тройка-модуля
    gpio.setup(troyka, gpio.OUT, initial = gpio.LOW)
    
    #Проведение измерений во время разряда конденсатора
    print('Разрядка конденсатора')
    while voltage > 256*0.02:
        voltage = adc()
        data.append(voltage)
        time.sleep(0.005)
        c += 1
        gpio.output(leds, decimal2binary(voltage))

    all_time = time.time() - start_time 

    print('Продолжительность эксперимента {}, Период измерения {}, Средняя частота дискретизации {}, Шаг квантования АЦП {}'.format(round(all_time, 2), round(all_time/c, 2), round(1/all_time/c, 4), 0.013))  

    #Запись данных в файл
    print('Запись данных')
    with open('/home/b04-203/Desktop/Mordvinova/data.txt', 'w') as f:
        for i in data:
            f.write(str(i) + '\n')
    with open('/home/b04-203/Desktop/Mordvinova/settings.txt', 'w') as f:
        f.write(str(round(1/all_time/c, 4)) + '\n')
        f.write('0.013')
    
    #Построение графика
    x = [i*all_time/c for i in range(len(data))]
    y = [i/256*3.3 for i in data]
    pyplot.plot(x,y)
    pyplot.xlabel('time')
    pyplot.ylabel('voltage')
    pyplot.show()

finally:
    gpio.output(dac, 0)
    gpio.output(leds, 0)
    gpio.cleanup()