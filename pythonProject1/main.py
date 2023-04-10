def matrix_from_file(file_name):
    file = open(file_name, 'r')
    line = list(map(int, file.readline().split()))
    length = len(line)
    if length < 2:
        return
    matrix = [[0 for j in range(length)] for i in range(length)]
    matrix[0] = line
    i = 1
    while True:
        line = list(map(int, file.readline().split()))
        if not line:
            break
        matrix[i] = line
        i += 1
    file.close()
    return matrix


def determinant(matrix, shlyp):
    count = len(matrix)
    if count == 1:
        return shlyp * matrix[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(count):
            m = matrix
            for j in range(1, count):
                buff = []
                for k in range(count):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + shlyp * determinant(m, sign * matrix[0][i])
    return answer
def main():
    write_answear_into_file(r"C:\Users\Алексей\Desktop\z1\output3.txt", str(determinant(matrix_from_file(r"C:\Users\Алексей\Desktop\z1\inputs\input3.txt"), 1)))

def write_answear_into_file(file_name, number):
    file = open(file_name, 'w')
    file.write(number)
    file.close()
main()
