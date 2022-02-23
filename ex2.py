def mirror(p):
    text = ''
    for i in range(len(p)-1, -1,-1):
        text += p[i]
    return text


per = input()
rez = mirror(per)

print(rez)
