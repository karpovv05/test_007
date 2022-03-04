from math import *


def fun(a, b):
    c2 = a ** 2 + b ** 2
    c = sqrt(c2)
    return c


ba, ac = int(input("ba= ")), int(input("ac= "))

bc = fun(ba, ac)
cd = int(input("cd= "))
bd=fun(bc, cd)
print(ba+ac+cd+bd)
