from math import *


def fun(x):
    za = cos(x*2) + sin(x-3)
    return za


fa = fun(int(input("a= ")))
fb = fun(int(input("b= ")))

if fa > fb:
    print('b=', fb)
else:
    print("a=", fa)
