import math

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

a1 = math.sqrt(a**2 + b**2)
b2 = (a + b) ** (1/7)
c3 = (a**12 + b**12) ** (1/3)

print(a1, b2, c3)

