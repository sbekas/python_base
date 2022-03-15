# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, date):
      __class__.date = date


    @classmethod
    def extract_date(cls):
        cls.date_list = cls.date.split('-')
        for el in cls.date_list:
            __class__.day = int(cls.date_list[0])
            __class__.month = int(cls.date_list[1])
            __class__.year = int(cls.date_list[2])
        # print(cls.date_list)

    @staticmethod
    def date_validator(day, month, year):
        days_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Определение високосного года
        visok_god = True
        if year % 4 != 0:
            visok_god = False
        elif year % 100 == 0:
            visok_god = False
            if year % 400 == 0:
                visok_god = True
            else:
                visok_god = False


        result = f'Ok.'


        if 0 < month <= 12:
            True
        else:
            result = f'Месяц задан неверно.'

        if 0 < day <= days_list[month]:
           result = f'Ok.'
        elif days_list[month] != 2:
            result = f'День задан неверно.'
            if day > 29:
                result = f'День задан неверно.'
            elif visok_god:
                result = f'Ok.'
        return result


date_1 = Date('03-01-2020')
print(date_1.date)
Date.extract_date()
print(Date.day)
print(Date.month)
print(Date.year)
Date.day += 2
date_2 = Date('07-01-2020')
print(Date.day)
print(date_2.day)
Date.extract_date()
print(date_2.day)
print(Date.day)


print(Date.date_validator(29, 2, 1100))  #Ошибка в дне. Год обычный
print(Date.date_validator(29, 2, 2024))  #Ok. Год високосный
print(Date.date_validator(25, 4, 1100))  #Ok. Год обычный
print(Date.date_validator(29, 2, 1992))  #Ok. Год високосный
print(Date.date_validator(29, 2, 1992))  #Ok. Год високосный
print(Date.date_validator(29, 2, 1980))  #Ok. Год високосный
print(Date.date_validator(32, 7, 1980))  #Ошибка в дне. Год високосный
print(Date.date_validator(31, 7, 1980))  #Ok. Год високосный
print(Date.date_validator(31, 6, 1978))  #Ошибка в дне. Обычный год
print(Date.date_validator(31, 2, 1978))  #Ошибка в дне. Обычный год
print(Date.date_validator(28, 2, 1978))  #Ok. Обычный год






