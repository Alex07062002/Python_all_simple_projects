def frequency_sort(items):
    items.sort()
    temp = []
    sort_dict = {x: items.count(x) for x in items}
    for k, v in sorted(sort_dict.items(), key=lambda x: x[1], reverse=True):
        temp.extend([k] * v)
    return temp


if __name__ == '__main__':
    array = [5, 3, 5, 8, 7, 7, 1, 8, 9, -1, 0, 8, -1, 3, 4, 77, 12, 34, 12, 8, 1, -1, 6, 5, 4, 37, 8, 64, 32, -1, -1]
    print(frequency_sort(array))



