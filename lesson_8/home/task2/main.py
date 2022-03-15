# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = input("Введите делимое: ")
b = input("Введите делитель: ")

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise DivZeroError("Вы ввели делитель 0! На ноль делить нельзя!")
    else:
        res = a / b
except ValueError:
    print("Вы ввели не число")
except DivZeroError as err:
    print(err)
else:
    print(f"Все хорошо. Ваш делитель: {b}\n {a} / {b} = {res:.2f}")