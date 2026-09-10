a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
c = float(input("Введите третью сторону: "))

perimeter = a + b + c
semi_perimeter = perimeter / 2
area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5

print("Периметр:", perimeter)
print("Полупериметр:", semi_perimeter)
print("Площадь:", area)
