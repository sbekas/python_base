# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(my_list)
num_add_str = input('Введите натуральное число: ')
num_add = int(num_add_str)
last_el_index = len(my_list) - 1
# print(last_el_index)

for el_str in my_list:
    el = int(el_str)
    el_index = my_list.index(el_str)
    # print(rating_list)
    if num_add > el:
        el_index_minus = el_index - 1   # по-идее интерпретатор должен выдать ошибку, типа out of index (-1), если ставить максимальное число
        print(f'Добавляем число {num_add} в {el_index} индекс')
        rating_list = my_list.copy()
        rating_list.insert(el_index, num_add)
        break
    elif num_add <= el and el_index == last_el_index: # пользователь вводит '2' - ставим знак '<='
        rating_list = my_list.copy()
        rating_list.append(num_add)
        print(f'Добавляем число {num_add} в {len(my_list)} индекс')

print(rating_list)
