from datetime import datetime
from sys import api_version

initial_price = 2000000

year_of_manufacture = int(input("Enter the year of manufacture: "))
current_mileage = int(input("Enter the current mileage: "))

current_year = datetime.now().year

age_of_car = current_year - year_of_manufacture
depreciation = age_of_car * 0.1
final_price = initial_price * (1 - depreciation)

if age_of_car > 0:
    avarage_annual_mileage = current_mileage / age_of_car
else:
    avarage_annual_mileage = current_mileage

print(f"- Інформація про автомобіль:")
print(f"- Рік випуску: {year_of_manufacture}")
print(f"- Вік автомобіля: {age_of_car}")
print(f"- Первісна вартість: {initial_price} uah")
print(f"- Пробіг автомобіля: {current_mileage} км")
print(f"- Середній річний пробіг: {avarage_annual_mileage:.0f} км/рік")
print(f"- Орієнтована поточна вартість: {final_price:.2f} грн")
