# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


result_list = [el for el in range(100, 1001, 2)]
print(result_list)
print(reduce(my_func, result_list))
#
# mult = 1
# for el in result_list:
#     mult *= el
#     #print(result_list.index[100])
#
# print(mult)