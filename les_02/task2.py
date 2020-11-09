# https://drive.google.com/file/d/1yauYrjV_VsvlN_-lNROW20s48JC12kRv/view?usp=sharing
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные
# цифры (4, 6 и 0) и 2 нечетные (3 и 5).
print('Введите натуральное число (целое, больше нуля)')
a = int(input())
even = 0
odd = 0
while True:
    n = a % 10
    a = a // 10
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    if a == 0:
        break
print('Четных: ', even, 'Нечетных: ', odd)
