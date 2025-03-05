def input_point():
    x = float(input("Введіть x: "))
    y = float(input("Введіть y: "))
    return (x, y)

def print_point(point):
    print(f"Координати точки: ({point[0]:.2f}, {point[1]:.2f})")

point = input_point()
print_point(point)
