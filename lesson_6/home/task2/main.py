# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asfalt_weight(self, ud_mass, thick):
        self._weight = self._length * self._width * ud_mass * thick / 1000
        return self._weight


mass = int(input(f'Введите удельную массу асфальта (кг/м2): '))
thick = int(input(f'Введите толщину дорожного полотна (см): '))
road_l = int(input(f'Введите длину дороги (м): '))
road_w = int(input(f'Введите ширину дороги (м): '))
thick_meters = thick / 100
road = Road(road_l, road_w)
print(f'На дорогу шириной {road_w}м и длиной {road_l}м требуется {road.asfalt_weight(mass, thick_meters)} тонн асфальта')

