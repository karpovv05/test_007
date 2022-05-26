# put your python code here
# p=input().split()
x = int(input())
l = list()
tot = 0

for i in range(x):
    tot += 1
    l.append(list())
    for j in range(x):

        if j!= tot-1 and j!=x-tot:
            l[i].append(0)
        else:
            l[i].append(1)

    print(*l[i])
