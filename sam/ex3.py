import math

def f(x):
    if x >= 0:
        return 0.5 - math.sqrt(abs(x)) ** 4
    else:
        return (math.sin(x**2) ** 2) / abs(x + 1)

x = float(input("Введіть значення x: "))

print(f"f({x}) = {f(x)}")
