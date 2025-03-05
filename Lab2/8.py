import math

precision = int(input("Введіть кількість знаків після коми: "))

print(f"√2 = {math.sqrt(2):.{precision}f}")
print(f"(2,5)^1.6 = {math.pow(2, 5)**1.6:.{precision}f}")
print(f"π + e = {math.pi + math.e:.{precision}f}")
