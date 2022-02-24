#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    list  = [arg_1, arg_2, arg_3]
    list.sort()
    sum_max = list[1] + list[2]
    return sum_max


print(my_func(5, 2, 4))
