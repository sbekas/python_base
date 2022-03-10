# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, title, param):
        self.title = title
        self.param = param

    def __str__(self):
        return f'{self.title}'

    @abstractmethod
    def necessary(self, param):
        pass


class Coat(Clothes):

    @property
    def necessary(self):
        v = int(self.param)
        return v/6.5 + 0.5


class Costume(Clothes):

    @property
    def necessary(self):
        h = int(self.param)
        return 2 * h + 0.3


coat = Coat('Пальто', 2)
print(f'На {coat} необходимо {coat.necessary:.2f}м ткани')
costume = Costume('Костюм', 2)
print(f'На {costume} необходимо {costume.necessary:.2f}м ткани')


print(coat.necessary + costume.necessary)
