# Определить, является ли год, который  ввел пользователь високосным или не високосным.

y = int(input("Введите порядковый номер года в виде четырехзначного числа: "))

if y % 4 == 0:
    print("Похоже, этот год високосный")
    if y % 100 == 0 and y % 400 != 0:
        print("Хотя все же нет, не високосный, поскольку кратен 100, но не кратен 400")
else:
    print("Год не является високосным")

print("#" * 30, "Второй вариант, нормальный: ", "#" * 30)

if y % 100 == 0 and y % 400 != 0:
    print("Этот год не високосный")
else:
    if y % 4 == 0:
        print("Этот год високосный")
    else:
        print("Этот год не високосный")