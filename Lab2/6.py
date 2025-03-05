import math

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))

log_xy = math.log(y) / math.log(x)  # Формула логарифма за довільною основою

print(f"log_{x}({y}) = {log_xy:.3f}")
