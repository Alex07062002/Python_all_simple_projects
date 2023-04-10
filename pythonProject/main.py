#Python 3.7.9

def read_matrix_from_file(file_name):
    file = open(file_name, 'r')
    string = list(map(int, file.readline().split()))
    length = len(string)
    if length < 2:
        return
    matrix = [[0 for j in range(length)] for i in range(length)]
    matrix[0] = string
    i = 1
    while True:
        string = list(map(int, file.readline().split()))
        if not string:
            break
        matrix[i] = string
        i += 1
    file.close()
    return matrix

def division(matrix):
    if len(matrix) > 2:
        det = 0
        for i in range(len(matrix[0])):
            new_arr = []
            for j in range(len(matrix[0])):
                if j != i:
                    new_arr.append([matrix[j][k] for k in range(1, len(matrix[0]))])
            sign = (-1 + 2 * ((i + 1) % 2))
            det += division(new_arr) * matrix[i][0] * sign
        return det
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    elif len (matrix) == 1:
        return matrix[0][0]

def main():
    write_det_into_file(r"output.txt", str(division(read_matrix_from_file(r"input10.txt"))))
# r перед путём к файлу необходима для того, чтобы обычную строку превратить в необработанную

def write_det_into_file(file_name, answer):
    file = open(file_name, 'w')
    file.write(answer)
    file.close()

main()
