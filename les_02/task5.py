# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке

i = 32
j = 0
while i <= 127:
    print(f'{i}-{chr(i)}', end='\t')
    i += 1
    j += 1
    if j % 10 == 0:
        print()
