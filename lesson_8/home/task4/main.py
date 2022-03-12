# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class Sklad:

    pass


class Technic:
    def __init__(self, mark, model, format):
        self.mark = mark
        self.model = model
        self.format = format
    pass


class Printer(Technic):
    def __init__(self, mark, model, format, type_printer, color): #type_printer - лазерный или чернильный, color - ч/б или цветной
        Technic.__init__(self, mark, model, format)
        self.type_printer = type_printer
    pass


class Scanner(Technic):
    def __init__(self, mark, model, format, type_scanner, color, resolution): #type_scanner - планшетный или ручной, color - ч/б или цветной
        Technic.__init__(self, mark, model, format)
        self.type_scanner = type_scanner
        self.color = color
        self.resolution = resolution
    pass


class Xerox(Technic):
    def __init__(self, mark, model, format, type_xerox): #type_xerox - рулонный или листовой, color - ч/б или цветной
        Technic.__init__(self, mark, model, format)
        self.type_xerox = type_xerox
    pass

xerox = Xerox('Xerox', 'Versalink C505', 'A3', 'List')
print(xerox)