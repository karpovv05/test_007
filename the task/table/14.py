p = 5

for i in range(4, -1, -1):
    p-=1
    dp=p
    for i2 in range(i + 1):
        print(dp, end=' ')
        dp-=1
    print()
