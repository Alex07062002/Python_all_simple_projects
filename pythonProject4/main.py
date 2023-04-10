import io_utils as IO
import arraysearch as Arrays


def test(search, array, name):
	avg = 0
	for i in range(len(array)):
		index, cmp = search(array, array[i])
		avg += cmp
		if index != i:
			print('Error index missmatch')
	print(f'{name} avg cmp {avg / len(array)}\n')
	IO.write_String(r'C:\Users\Алексей\Desktop\Дискретка\z3\output1.txt', f'{name} avg cmp {avg / len(array)}\n')


if __name__ == '__main__':
	inp_arr = IO.read_array(r'C:\Users\Алексей\Desktop\Дискретка\z3\input.txt')

	test(Arrays.index_of, inp_arr, 'Linaer')
	test(Arrays.binary_search, inp_arr, 'Binary')
	test(Arrays.interpolation_search, inp_arr, 'Interpolar')