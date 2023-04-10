import math


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j

def SelectPart(list, k):
    left = 0
    right = len(list)
    found = False
    while found == False:
        v = partition(list, left, right)
        if (k < v):
            right = v - 1
        elif (k == v):
            found == True
            return list[v]
        elif (k > v):
            left = v + 1
        if (found == True): break;


def insertion_sort(alist,left,right):
    for i in range(left, right):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

w =5
def SelectOpt(list,k,left,right):
    while True:
        d = right-left;
        if (d<=w):
            insertion_sort(list,left,right)
            return list[left+k]
            break;
        dd = int(math.floor(d/w))
        for i in range(1,dd+1,1):
            insertion_sort(list, left+(i-1)*w,left+i*w-1)
            list[left+i-1],list[left+(i-1)*w+math.ceil(w/2)-1] = list[left+(i-1)*w+math.ceil(w/2)-1], list[left+i-1]
        v = SelectOpt(list,math.ceil(dd/2),left,left+dd-1)
        list[left], list[v] = list[v], list[left]
        v = partition(list,left,right)
        temp = v-left
        if (k < temp):
            right = v - 1
        elif (k == v):
            return list[v]
        elif (k > v):
            k = k-temp
            left = v + 1



if __name__ == '__main__':
    inp = open(r'C:\Users\Алексей\Desktop\Дискретка\z7\input.txt')
    k = int(inp.readline())
    list = inp.readline().split(" ")
    inp.close()
    inp = open(r'C:\Users\Алексей\Desktop\Дискретка\z7\output.txt',"w")
    inp.write(f'{SelectPart(list,k)}, {SelectOpt(list,k,0,len(list)-1)}')
    inp.close()
