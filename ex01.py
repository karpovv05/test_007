from random import *

line=int(input("Символов в строке "))
col=int(input("Кол во строк "))


num1=int(input("От скольки "))
num2=int(input("До скольки "))

matrix = []

for c in range(col):
    matrix.append([])
    for l in range(line):
        matrix[c].append(randint(num1,num2))

print(matrix)