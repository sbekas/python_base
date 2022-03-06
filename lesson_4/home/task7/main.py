# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count


def factorial(fact):
    result = 1
    for el in count(1):
        result *= el
        if el == fact + 1:
            break
        yield result


n = int(input('Введите число n: '))
factorials_list = []
for el in factorial(n):
    factorials_list.append(el)

print(factorials_list)


