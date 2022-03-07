from math import *


def fun(x, n):
    rez = x ** n / n
    return rez


z = 0
x = int(input("x="))
for i in range(3):
    z += fun(x, int(input('n')))

print(z)
