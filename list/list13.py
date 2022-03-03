def fun(x):

    if 100<=x<=999:
        rez=''
        rez+= str(x%10)+str(x//10%10)+str(x//100)
        return int(rez)
    else: return x

print(fun(int(input())))
