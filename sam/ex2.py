import math

print("Програма для розрахунку Z")

print("\nВведіть дані:")
x = float(input("Введіть значення x: "))
t = 1

chiselnik = 9 * math.pi * t + 10 * math.cos(x)
znamenik = math.sqrt(t) - abs(math.sin(t))
z = (chiselnik / znamenik) * math.exp(x)

print(f"Результат Z для x = {x}, t = {t}: {z:.3f}")

