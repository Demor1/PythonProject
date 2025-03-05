a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

min_value = min(a, b, c)

max_value = max(a, b, c)

if max_value % 2 == 0:
    parne = "парне"
else:
    parne = "непарне"

print(f"Мінімальне число:", min_value)
print(f"Максимальне число: {max_value} ({parne})")
