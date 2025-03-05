a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

N = int(input("Введіть N: "))

result = []
for x in [a, b, c]:
    if 1 <= x <= N:
        result.append(x)

print("Числа у межах [1, N]:", result)
