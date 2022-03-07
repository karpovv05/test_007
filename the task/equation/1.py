from math import *

a,b,x=int(input('a')),int(input('b')),int(input('x'))
if x**2-5*x<0:
    print(a+b)
if 0<=(x**2-5*x)<10:
    print(a-b)
if x**2-5*x>=10:
    print(a*b)
