def max(a, b):
    if a > b:
        return a
    else:
        return b


x = int(input())
y = int(input())

print(max(x,y*2-x)+max(5*x+3*y,y))