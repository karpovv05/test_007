def min(a,b):
    if a<b:
        return a
    else:
        return b


x = int(input())
y = int(input())
z=int(input())
v=int(input())

r=min(min(x,y),min(z,v))

print(r)