from math import *


def fun(x):
    za = x ** 3 - sin(x)
    return za


fa = fun(int(input("a= ")))
fb = fun(int(input("b= ")))

if fa < fb:
    print('b=', fb)
else:
    print("a=", fa)
