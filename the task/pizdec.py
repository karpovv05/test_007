import pprint

board = []
az = list('abcdefgh')
num = list('12345678')
cou = -1
for al in range(7, -1, -1):
    board.append([])
    cou += 1
    for di in range(7, -1, -1):
        board[cou].append(az[al] + num[di])
# ---------------
ln = []
kk = 8
xco = -1
for i in range(kk):
    ln.append([])
    xco += 1
    for x in range(kk - 1, -1, -1):
        ln[xco].append(board[x][xco])
board = ln
lnew = []
poz = input()

for i in range(8):
    lnew.append([])
    for j in range(8):
        if board[i][j] != poz:

            lnew[i].append('.')
        else:
            lnew[i].append('N')
            zn = i, j

y, x = zn[0], zn[1]

if 7 >= y - 2 >= 0 and 7 >=x - 1 >= 0:
    lnew[y - 2][x - 1] = '*'
if 7 >= y - 2 >= 0 and 7 >=x + 1 >= 0:
    lnew[y - 2][x + 1] = '*'
if 7 >= y - 1 >= 0 and 7 >=x + 2 >= 0:
    lnew[y - 1][x + 2] = '*'
if 7 >= y + 1 >= 0 and 7 >=x + 2 >= 0:
    lnew[y + 1][x + 2] = '*'
if 7 >= y + 2 >= 0 and 7 >=x + 1 >= 0:
    lnew[y + 2][x + 1] = '*'
if 7 >= y + 2 >= 0 and 7 >=x - 1 >= 0:
    lnew[y + 2][x - 1] = '*'
if 7 >= y - 1 >= 0 and 7 >=x - 2 >= 0:
    lnew[y - 1][x - 2] = '*'
if 7 >= y + 1 >= 0 and 7 >=x - 2 >= 0:
    lnew[y + 1][x - 2] = '*'


for i in lnew:
    print(*i)
