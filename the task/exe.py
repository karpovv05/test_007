x = int(input())
t = []
num = 0
tot = 0
per = -99999
for i in range(x):
    tot += 1
    t.append(input().split())

for l in range(x):
    if x % 2 == 1:
        if l < x // 2 + 1:
            num -= 1
            for b in range(-1,num-1,-1):
                if int(t[l][b]) > per:
                    per = int(t[l][b])
        else:
            num += 1
            for b in range(-1,num-1,-1):
                if int(t[l][b]) > per:
                    per = int(t[l][b])
    if x % 2 == 0:
        if l < x // 2 and x % 2 == 0:
            num -= 1
            for b in range(-1,num-1,-1):
                if int(t[l][b]) > per:
                    per = int(t[l][b])
        else:
            for b in range(-1,num-1,-1):
                if int(t[l][b]) > per:
                    per = int(t[l][b])
            num += 1
print(per)