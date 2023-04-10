def insertion_sort(array):
    cmp = 0
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            cmp += 1
        array[j + 1] = temp
    write_String(r'C:\Users\Алексей\Desktop\Дискретка\z4\output1.txt', f'{array}\n Число сравнений:  {cmp}\n')
    return array, cmp


def read_array(filename):
    f = open(filename, 'r')
    return list(map(int, f.readline().split()))


def write_String(filename, String):
    f = open(filename, 'w')
    f.write(String)


if __name__ == '__main__':
    inp_arr = read_array(r'C:\Users\Алексей\Desktop\Дискретка\z4\input.txt')
    print('Было ',inp_arr)
    print('Стало ',insertion_sort(inp_arr))
