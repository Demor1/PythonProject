import math

def check_real_value(value):
    if math.isnan(value):
        return "Значення є NaN"
    elif math.isinf(value):
        if value > 0:
            return "Значення є +∞"
        else:
            return "Значення є -∞"
    else:
        return f"Число: {value}"

value = float(input("Введіть дійсне число: "))
print(check_real_value(value))
