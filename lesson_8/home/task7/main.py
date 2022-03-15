# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

# z = a + bi
# y = c + di
# z + y = (a + c) + (b + d)i
# z * y = (ac - bd) + (ad + bc)i


class ComplexNum:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        if self.img < 0:
            return f'{self.real} - {abs(self.img)}i'
        else:
            return f'{self.real} + {self.img}i'

    def __add__(self, other):
        com_real = self.real + other.real
        com_img = self.img + other.img
        return ComplexNum(com_real, com_img)

    def __mul__(self, other):
        com_real = self.real * other.real - self.img * other.img
        com_img = self.real * other.img + self.img * other.real
        return ComplexNum(com_real, com_img)


a = ComplexNum(-2, -6)
b = ComplexNum(-13, -1)

c = a + b
d = a * b
print(f'a = {a}')
print(f'b = {b}')
print(f'a + b = {c}')
print(f'a * b = {d}')

e = ComplexNum(+8, +3)
f = ComplexNum(-13, -1)
m = e + f
n = e * f
print(f'e = {e}')
print(f'f = {f}')
print(f'e + f = {m}')
print(f'e * f = {n}')


o = ComplexNum(4.58, 0.03)
p = ComplexNum(-13.4, 0.23)
r = o + p
s = o * p
print(f'o = {o}')
print(f'p = {p}')
print(f'o + p = {r}')
print(f'o * p = {s}')