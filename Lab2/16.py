def format_date(day, month, year):
    return f"{day:02}.{month:02}.{year % 100:02}"

day = int(input("Введіть день: "))
month = int(input("Введіть місяць: "))
year = int(input("Введіть рік: "))

print("Дата у форматі dd.mm.yy:", format_date(day, month, year))
