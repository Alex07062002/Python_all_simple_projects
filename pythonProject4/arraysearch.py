def index_of(list, target):
	cmp = 0
	for i in range(len(list)):
		cmp += 1
		if target==list[i]:
			return i, cmp
	return -1, cmp


def binary_search(list, target):
	cmp = 0
	start, end = 0, len(list)
	while start < end:
		cmp += 1
		middle = (start + end) // 2
		if list[middle] > target:
			end = middle
		elif list[middle] < target:
			start = middle
		else:
			return middle, cmp
	return -1, cmp


def interpolation_search(arr, x):
	cmp = 0
	start, end = 0, len(arr) - 1
	while start < end:
		cmp += 1
		pos = start + (end - start) * (x - arr[start]) // (arr[end] - arr[start])
		if arr[pos] > x:
			start = pos
		elif arr[pos] < x:
			end = pos
		else:
			return pos, cmp
	return -1, cmp
