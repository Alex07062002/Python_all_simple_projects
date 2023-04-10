import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator



def read_column(n): #чтение файлика
    with open(r"C:\Users\Алексей\Downloads\emg_all_features_labeled.csv", "r") as csv_file:  #открытие emg.csv для чтения при помощи csv_file
        csv_reader = csv.reader(csv_file, delimiter=',') #csv_reader возвращает объект reader, который построчно итерирует csvfile.Каждая строка, считанная из файла csv, возвращается в виде списка строк. разделяется при помощи delimiter=','
        return [float(line[n]) for line in csv_reader] #вернули список из чисел


def analyse_freq(values, window, med):
    activity_list = [] #пустой массив
    for i in range(0, len(values) - window, window):#проход по элемента от 0 до len(values) - window с шагом window
        avg = np.average(values[i:i + window]) #вычисляет среднее арифметическое взвешенное значений элементов массива.
        activity_list.append(avg > med) #добавление  в массив элемента, с условием avg > med (знаение больше среднего)
    return activity_list





def plot(dots, med, activity_list, window):
    fig, ax = plt.subplots() #создали объект типа  Figure – это самый важный внешний контейнер для графики matplotlib, который может включать в себя несколько объектов Axes. Axes (оси) - индивидуальный график или диаграммой
    ax.yaxis.set_major_locator(MaxNLocator(20)) #изменение меток сетки, установленной по умолчанию на ось у. set_major_locator() – управление рисками крупной сетки. локатор MaxNLocator выполняет самостоятельную разбивку интервала на число рисок не более 20
    ax.plot(dots,color='green') #отрисовка
    ax.plot(med,color="magenta")#отрисовка
    fig.set_size_inches(15, 7) #изменение размера после создания
    for i in range(len(activity_list)):#проход по массиву
        if activity_list[i]:
            ax.axvspan(i * window, (i + 1) * window, alpha=0.5, color='orange')#трисовка прямоугольников для обозначения максимума
    plt.gca().invert_yaxis()
    plt.show()


def main():
    column = read_column(16)#список чисел , прочитанных из файла
    window = 200 #размер
    med = np.median(column) #вычисление медианы  из списка column
    meds = [med for _ in range(len(column))]#вычисление среднего значения для каждой строки
    activity_list = analyse_freq(column, window, med)
    plot(column, meds, activity_list, window)


if __name__ == '__main__':
    main()
