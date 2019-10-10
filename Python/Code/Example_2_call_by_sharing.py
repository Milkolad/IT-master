def f(a,b):
    a += b
    return a

x = 1
y = 2
print(f(x,y),x,y)

x = [1, 2]
y = [3, 4]
print(f(x,y),x,y)


x = (1, 2)
y = (3, 4)
print(f(x,y),x,y)