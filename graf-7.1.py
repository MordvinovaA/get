import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'montserrat'
fig, ax = plt.subplots()
data = []
#d = float(input('ведите частоту отображений маркеров: '))
# Запись данных из файлов
with open('data.txt', 'r') as f:
    data = list(map(int, f.readlines()))
with open('settings.txt', 'r') as f:
    ch_disc = float(f.readline())
    shag_kvant = float(f.readline())
    zar_time = round(float(f.readline()), 2)
    raz_time = round(float(f.readline()), 2)
all_time = zar_time + raz_time

'''if d != 1:
    ost = int(len(data) * d)
    ybr = len(data) - ost
    sh = int(len(data) / ybr)
    print(sh)
    print(ost)
    print(ybr)
    i = sh
    while i < len(data):
        data.pop(i)
        print(data)
        i += sh
'''

if data != []:
    # Построение графика
    x = [i * all_time / len(data) for i in range(len(data))]
    y = [i / 256 * 3.3 for i in data]
    plt.plot(x, y, c='blue', label='V(t)', linewidth=2 )
    plt.scatter(x, y, s=25, c='blue', marker='o')
    plt.xlabel('Время, с', fontsize=20)
    plt.ylabel('Напряжение, В', fontsize=20)
    ax.minorticks_on()
    ax.grid(True, which='both')
    ax.grid(which='major', color='k', linewidth=1)
    ax.grid(which='minor', color='k', linestyle=':')
    plt.title('Процесс заряда и разряда конденсатора в RC-цепочке ', fontsize=33, wrap=True, pad=20)
    plt.legend(loc = 'upper right', ncol=20, prop={'size': 30})
    plt.axis([round(min(x), 1), round(max(x), 1), round(min(y), 1), round(max(y), 1)])
    ax.text(40, 2, 'Время заряда = {} с \n\nВремя разряда = {} с'.format(zar_time, raz_time), fontsize=20)
    plt.show()


