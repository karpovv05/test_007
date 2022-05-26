# put your python code here
import random

l=list()
game=[]
for i in range(5):
    game.append([])
    while len(game[i]) !=5:
        p = random.randrange(10, 76)
        if p not in l:
            l.append(p)
            game[i].append(str(p))
        if i==2 and len(game[i])==3:
            game[2][2] = '0'+' '
    print(*game[i])



