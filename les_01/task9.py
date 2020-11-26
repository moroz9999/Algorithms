# Вводятся три разных числа. Определить, какое из них является средним
# (больше одного, но меньше другого)

a, b, c = map(int, input("Введите три разных числа через пробел: ").split())

if a > b:
    if a > c:
        print(b if b > c else c)
    else:
        print(a)
else:
    if b > c:
        print(c if c > a else a)
    else:
        print(b)
