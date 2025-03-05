import math

a, b = 2, 3  # Прикладні значення
r = 5

expr1 = math.log(math.sqrt(a**2 + b**2))
expr2 = math.sin((a + b)**(1/7))
expr3 = math.cos(math.sqrt(a**2 + b**2)**(12))
expr4 = 1 / math.tan(math.sqrt(a) - math.sqrt(b))

print(f"ln√(a² + b²) = {expr1:.3f}")
print(f"sin((a + b)^(1/7)) = {expr2:.3f}")
print(f"cos(√(a² + b²)^12) = {expr3:.3f}")
print(f"ctg(√a - √b) = {expr4:.3f}")
