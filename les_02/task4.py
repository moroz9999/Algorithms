# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
n = int(input("Введите количество элементов последовательности: "))
sum = 0
i = 1
el = 1
while i < n:
    sum += el
    el /= -2
    i += 1
print(round(sum, 4))
