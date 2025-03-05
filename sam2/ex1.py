import math


def main_menu():
    while True:
        print("\nГоловне меню:")
        print("1. Координати точки (2D, 3D)")
        print("2. Обчислення математичних виразів")
        print("3. Периметр трикутника")
        print("4. Робота з колом")
        print("5. Використання функцій модуля math")
        print("6. Форматування чисел")
        print("7. Персональне вітання")
        print("8. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            handle_coordinates()
        elif choice == "2":
            calculate_expressions()
        elif choice == "3":
            calculate_triangle_perimeter()
        elif choice == "4":
            circle_operations()
        elif choice == "5":
            math_functions()
        elif choice == "6":
            format_numbers()
        elif choice == "7":
            greet_user()
        elif choice == "8":
            print("Вихід з програми.")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")


def handle_coordinates():
    print("\n[Робота з координатами]")
    dim = input("Введіть розмірність (2D або 3D): ")
    if dim == "2D":
        x = float(input("Введіть x: "))
        y = float(input("Введіть y: "))
        print(f"Координати точки: ({x}, {y})")
    elif dim == "3D":
        x = float(input("Введіть x: "))
        y = float(input("Введіть y: "))
        z = float(input("Введіть z: "))
        print(f"Координати точки: ({x}, {y}, {z})")
    else:
        print("Некоректне значення. Спробуйте ще раз.")


def calculate_expressions():
    print("\n[Обчислення математичних виразів]")
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    result1 = math.log(a ** 2 + b ** 2)
    result2 = math.sin((a + b) ** (1 / 7))
    result3 = math.cos(a ** 12 + b ** 12) ** 3
    print(f"ln(a² + b²) = {result1:.4f}")
    print(f"sin((a + b)^(1/7)) = {result2:.4f}")
    print(f"cos³(a¹² + b¹²) = {result3:.4f}")


def calculate_triangle_perimeter():
    print("\n[Розрахунок периметра трикутника]")
    a = float(input("Введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    c = float(input("Введіть сторону c: "))
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        print(f"Периметр трикутника: {perimeter:.2f}")
    else:
        print("Некоректні сторони трикутника!")


def circle_operations():
    print("\n[Робота з колом]")
    L = float(input("Введіть довжину кола: "))
    r = L / (2 * math.pi)
    S = math.pi * r ** 2
    print(f"Радіус: {r:.4f}")
    print(f"Площа: {S:.4f}")


def math_functions():
    print("\n[Функції модуля math]")
    x = float(input("Введіть число: "))
    print(f"Квадратний корінь: {math.sqrt(x):.4f}")
    print(f"Натуральний логарифм: {math.log(x):.4f}")
    print(f"Синус: {math.sin(x):.4f}")
    print(f"Косинус: {math.cos(x):.4f}")
    print(f"Тангенс: {math.tan(x):.4f}")
    print(
        f"Факторіал (для цілих чисел): {math.factorial(int(x)) if x >= 0 and x.is_integer() else 'Недійсне значення'}")
    print(f"Експонента: {math.exp(x):.4f}")


def format_numbers():
    print("\n[Форматування чисел]")
    num = float(input("Введіть число: "))
    decimals = int(input("Кількість знаків після коми: "))
    print(f"Fixed-point формат: {num:.{decimals}f}")
    print(f"Scientific формат: {num:.{decimals}e}")


def greet_user():
    print("\n[Персональне вітання]")
    name = input("Введіть ім'я: ")
    surname = input("Введіть прізвище: ")
    print(f"Привіт, {name} {surname}!")


def equation_of_line():
    print("\n[Рівняння лінії]")
    a = float(input("Введіть коефіцієнт a: "))
    b = float(input("Введіть коефіцієнт b: "))
    print(f"Рівняння: {a}x + {b} = 0")


if __name__ == "__main__":
    main_menu()
