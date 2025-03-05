import math

def calculate_expression(x, y, z):
    return math.exp(x) + 2 * y * z

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
z = float(input("Введіть z: "))

result = calculate_expression(x, y, z)
print(f"Результат виразу e^x + 2yz: {result:.3f}")
