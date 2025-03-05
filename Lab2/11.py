import math

def compute_value(x, y):
    return (x + math.pi) / (x**2 + y**4 + math.exp(2))

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))

result = compute_value(x, y)
print(f"Результат виразу (x + π) / (x² + y⁴ + e²): {result:.3f}")
