# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
def get_revers(m, r):
    n = m % 10
    k = m // 10
    r = r + str(n)
    if k != 0:
        return get_revers(k, r)
    else:
        return int(r)


print('Введите натуральное число (целое, больше нуля)')
a = int(input())
s = ''  # Переменная для сбора цифр в обратном порядке
arev = get_revers(a, s)
print(arev)