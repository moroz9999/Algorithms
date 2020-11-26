# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9

res = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0,}
for i in range(2, 100):
    krat = 0
    for j in range(2, 10):
        if i // j > 0 and i % j == 0:
            res[j] += 1
print(res)

# Метод заполнения словаря ключами с одинаковыми значениями:

# keys_ = (2, 3, 4, 5, 6, 7, 8, 9)
# val = 0
# res = dict.fromkeys(keys_, val)
# print(res)
