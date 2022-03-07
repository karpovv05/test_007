from math import *


def fun(x):
    rez = (sqrt(x) + x )/2
    return rez


z=fun(int(input()))+fun(int(input()))+fun(int(input()))


print(z)