def min(a,b):
    if a<b:
        return a
    else:
        return b

x=int(input())
y=int(input())


z=min(x*3,y*2)+min(x-y,x+y)

print(z)