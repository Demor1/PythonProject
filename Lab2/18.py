def compute_function(a, x):
    return abs(x**5 + abs(a*x - x**3) - a) + a*x**2 + a**8

a = float(input("Введіть a: "))
x = float(input("Введіть x: "))

print(f"Результат f(a, x): {compute_function(a, x):.3f}")
