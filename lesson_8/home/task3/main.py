# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.


class ListNumError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
num = input('Введите число (для остановки ввода наберите "stop"): ')
my_list = []
my_list = [str(el) for el in range(0, 10)]


while num != 'stop':
    try:
        for el in list(num):
            # print(my_list.count(el))
            if my_list.count(el) == 0:
                raise ListNumError('Вы ввели не число. Повторите ввод')
            # else:
            #     print(el)
            #     print(my_list)
    except ListNumError as err:
        print(err)
    else:
        num_list.append(int(num))
    num = input('Введите число (для остановки ввода наберите "stop"): ')

print(num_list)
