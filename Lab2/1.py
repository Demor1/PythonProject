# Варіант а)
def f(a):
    a += 1
    return a

def g(x):
    x = 2
    return x

a = 3
b = 4
print(f(a), g(b), a, b)

# Варіант б)
def f1(x, y):
    x = x + y
    x += 1
    y -= 1
    tmp = f2(x, x, y)
    print(x, y, z)
    return tmp

def f2(x, y, z):
    tmp = x + y + z
    x = y = z = 0
    return tmp

x = 0
y = 1
z = 2
res = f1(y, x)
print(x, y, z, res)

# Варіант в)
def f1(x, y, z):
    x -= 1
    y += 1
    z += 2
    print(x, y, z)
    tmp = f2(x, y, z)
    return tmp

def f2(x, y, z):
    x, y, x, z, y = x, y, z, y, z
    print(x, y, z)
    return x + y + z

x = 0
y = 1
z = 2
res = f1(x, y, z)
print(x, y, z, res)
