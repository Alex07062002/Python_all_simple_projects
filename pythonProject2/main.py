import sympy
import math
from sympy import symbols
import functools


def cmp_limit(f0, f1):
    limitExpr = sympy.limit(f1 / f0, n, sympy.oo)
    print(limitExpr)  # just for debug
    if limitExpr > 0:
        return -1
    if limitExpr < 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    n = symbols('n')
    funct0 = math.sqrt(2) ** math.log(n, 2)
    funct1 = n ** 2
    funct2 = math.factorial(n)
    funct3 = math.factorial(math.log(n, 2))
    funct4 = (3 / 2) ** n
    funct5 = n ** 3
    funct6 = (math.log(n) / math.log(2)) ** 2
    funct7 = math.log(math.factorial(n)) / math.log(2)
    funct8 = 2 ** 2 ** n
    funct9 = n ** (1 / (math.log(n) / math.log(2)))
    funct10 = math.log(math.log(n))
    funct11 = n * 2 ** n
    funct12 = n ** math.log(math.log(n, 2), 2)
    funct13 = math.log(n)
    funct14 = 1
    funct15 = 2 ** math.log(n, 2)
    funct16 = math.log(n, 2) ** math.log(n, 2)
    funct17 = math.exp(n)
    funct18 = 2 * math.factorial(n)
    funct19 = math.sqrt(math.log(n, 2))
    funct20 = 2 ** math.sqrt(math.log(n, 2))
    funct21 = n * math.log(n, 2)
    funct22 = 2 ** n
    funct23 = n
    funct = [funct0, funct1, funct2, funct3, funct4, funct5, funct6, funct7, funct8, funct9, funct10, funct11, funct12,
             funct13, funct14, funct15, funct16, funct17, funct18, funct19, funct20, funct21, funct22, funct23]
    print(sorted(funct, key=functools.cmp_to_key(cmp_limit)))
