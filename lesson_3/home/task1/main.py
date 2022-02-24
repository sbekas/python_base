#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(dividend, divider):
    if divider == 0:
        return 'Ошибка, деление на 0'
    else:
        division = dividend / divider
#        division = dividend // divider
        return division

print(div(4.2, 2))
print(type(div(4, 2)))
print(type(div(4.2, 2)))
print(div(0.2, 0.0))
