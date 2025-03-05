from decimal import Decimal
a = (Decimal("10.001") ** 145) * (Decimal("13.001") ** 149) / ((Decimal("9.001") ** 155) * (Decimal("11.001") ** 179))
b = (Decimal("10.001") ** 345) * (Decimal("13.001") ** 249) / ((Decimal("9.001") ** 355) * (Decimal("11.001") ** 269))
c = (Decimal("20") / Decimal("3")) * (Decimal("12") / Decimal("5")) * (Decimal("11") / Decimal("7"))
d = (Decimal("12.11") * Decimal("71")) / (Decimal("3.5") * Decimal("9"))
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
