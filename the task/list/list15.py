from math import *

def fun(a,b,c):
    p=(a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    return s
r=0
for i in range(3):
    r+=fun(int(input()),int(input()),int(input()))

print(r)