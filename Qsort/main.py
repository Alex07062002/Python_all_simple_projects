
def cmp_int(a, b):
	return a - b


def qsort_swaps(array, cmp):
	return _qsort_swaps(array, 0, len(array) - 1, cmp)


def _qsort_swaps(array, low, high, cmp):
	swaps = 0
	if low in range(0, len(array)) and high in range(0, len(array)) and low < high:
		pivot, swaps = _partition_swaps(array, low, high, cmp)
		swaps += _qsort_swaps(array, low, pivot - 1, cmp)
		swaps += _qsort_swaps(array, pivot + 1, high, cmp)
	return swaps


def _partition_swaps(array, low, high, cmp):
	pivot = array[high]
	i = low
	swaps = 0
	for j in range(low, high):
		if cmp(array[j], pivot) < 1:
			array[i], array[j] = array[j], array[i]
			swaps += 1
			i += 1
	if i in range(0, high + 1):
		array[i], array[high] = array[high], array[i]
		swaps += 1
	return i, swaps


def qsort(array, cmp):
	return _qsort_swaps(array, 0, len(array) - 1, cmp)


def _qsort(array, low, high, cmp):
	if low in range(0, len(array)) and high in range(0, len(array)) and low < high:
		pivot = _partition(array, low, high, cmp)
		_qsort_swaps(array, low, pivot - 1, cmp)
		_qsort_swaps(array, pivot + 1, high, cmp)


def _partition(array, low, high, cmp):
	pivot = array[high]
	i = low
	for j in range(low, high):
		if cmp(array[j], pivot) < 1:
			array[i], array[j] = array[j], array[i]
			i += 1
	if i in range(0, high + 1):
		array[i], array[high] = array[high], array[i]
	return i

class scanner(object):
	def __init__(self, filename):
		self.f = open(filename, 'r')

	def read_array(self):
		return list(map(int, self.f.readline().split()))

	def read_matrix(self, size):
		return [list(map(int, self.f.readline().split())) for _ in range(size)]

	def read_int(self):
		return int(self.f.readline())

	def close(self):
		self.f.close()


def gen_array(length):
	array = []
	for i in range(0, length):
		array.append(i+1)
	return array


def get_permutations(array):
	permutations = []
	permutation = []
	chosen = [False for i in range(len(array))]

	def get_permutation():
		if len(permutation) == len(array):
			permutations.append(permutation.copy())
		else:
			for i in range(len(chosen)):
				if chosen[i]:
					continue
				chosen[i] = True
				permutation.append(array[i])
				get_permutation()
				chosen[i] = False
				permutation.pop()

	get_permutation()
	return permutations


if __name__ == '__main__':
	inp = scanner(r'C:\Users\Алексей\Desktop\Дискретка\z6\input.txt')
	n = inp.read_int()
	src = gen_array(n)

	permutations = get_permutations(src)
	res = list(map(lambda a: (a, qsort_swaps(a.copy(), cmp_int)), permutations))
	res.sort(key=lambda a: a[1])

	for arr, swaps in res:
		print(f'{arr}, Число сравнений: {swaps}')

	inp.close()
