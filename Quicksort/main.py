import itertools

def permutations(number):
    spam = list(range(1, number + 1))
    return list(itertools.permutations(spam))

class scanner(object):
	def __init__(self, filename):
		self.f = open(filename, 'r')
	def read_int(self):
		return int(self.f.readline())


if __name__ == '__main__':
	inp = scanner(r'C:\Users\Алексей\Desktop\Дискретка\z6\input.txt')
	n = inp.read_int()
	if (n != 2):
		if (n == 1):
			spam = list(range(1, n + 1))
			print(f'{spam},Количество сравнений: 0, так как массив состоит из 1 элемента')
		else:
			spam = list(range(1, n + 1))
			print(spam)
	if (n == 2):
		spam = list(range(1, n + 1))
		print(list(itertools.permutations(spam)))




