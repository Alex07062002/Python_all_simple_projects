class Entrant:
    def __init__(self, name, russian, maths, physics) -> None:
        self.name = name
        self.russian = russian
        self.maths = maths
        self.physics = physics

    def total_score(self):
        return self.russian + self.maths + self.physics

    def __str__(self):
        return self.name + ' ' + str(self.russian) + ' ' + str(self.maths) + ' ' + str(self.physics) + ' ' + str(
            self.total_score())


def from_entrant_to_student(list_entrant, N):
    list_entrant.sort(key=lambda x: (x.total_score(), x.maths, x.physics), reverse=True)
    return list_entrant[0:N]


if __name__ == '__main__':
    list1 = [Entrant("CAS", 100, 12, 35), Entrant("ASC", 89, 26, 32), Entrant("SCA", 100, 80, 30),
             Entrant("SCF", 100, 80, 55), Entrant("SAF", 100, 55, 80), Entrant("SDA", 95, 30, 22),
             Entrant("SGT", 78, 26, 43)]
    list_stud = from_entrant_to_student(list1, 5)
    for entrant in list_stud:
        print(entrant)

# задача 4:
# split по "<", начиная с "<" если в конце есть ">" то:
# проверка внутри <...> (substring) допустимые значения (match) "A-Za-z0-9"+"/"
# 1 и 2 пункты -> гарант html-тега
# Замена тега на пробел
