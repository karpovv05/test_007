def fun(x):

    if 10<=x<=99:
        rez=''
        rez+= str(x%10)+str(x//10)
        return int(rez)
    else: return x

print(fun(int(input())))
