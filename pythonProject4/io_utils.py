def read_array(filename):
    f = open(filename, 'r')
    return list(map(int, f.readline().split()))


def write_String(filename, String):
    f = open(filename, 'a')
    f.write(String)
