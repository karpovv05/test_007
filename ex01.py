from random import *

array = []
for i in range(21):
    array.append(randint(-100, 101))

for l in range(21):
    if -6 < array[l] < 28:
        print(array[l])
