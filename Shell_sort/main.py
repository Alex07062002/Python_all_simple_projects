import math


def inter(passes, string):
    if string == "first":
        h = int(math.pow(2, passes) - 1)
        return h
    else:
        h = 0
        h += int(math.pow(3, passes - 1))
        return h


def countMax(array, string):
    if string == "first":
        return int(math.floor(math.log2(len(array))))
    else:
        return int(math.floor(math.log(2 * len(array) + 1, 3) - 1))


def shellSort(array, string):
    cmp = 0
    n = len(array)
    k = countMax(array, string)
    interval = inter(k, string)
    while k > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                cmp += 1
            else:
                if j >= interval:
                    cmp += 1
            array[j] = temp
        k -= 1
        interval = inter(k, string)
    write_String(r'C:\Users\Алексей\Desktop\Дискретка\z5\output1.txt', f'{array}\n Число сравнений:  {cmp}\n')
    return array, cmp


def read_array(filename):
    f = open(filename, 'r')
    return list(map(int, f.readline().split()))


def write_String(filename, String):
    f = open(filename, 'a')
    f.write(String)


if __name__ == '__main__':
    inp_arr = read_array(r'C:\Users\Алексей\Desktop\Дискретка\z5\input10.txt')
    print(shellSort(inp_arr, "first"))
    inp_arr = read_array(r'C:\Users\Алексей\Desktop\Дискретка\z5\input10.txt')
    print(shellSort(inp_arr, "second"))
