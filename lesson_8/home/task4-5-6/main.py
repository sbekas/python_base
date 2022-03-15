# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class Storage:
    def __init__(self):
        self.technics = {}

    def take_technic(self, technics):
        for key, value in technics.items():
            if key in self.technics:
                self.technics[key] += value
            else:
                self.technics[key] = value

        self.technics = {}

    def give_technic_to_department(self, department, technic):
        if technic.id in self.technics and self.technics.technic_id > 0:
            if department.take_technic(technic):
                self.technics[technic.id] -= 1

    def take_technic_from_department(self, department, technic):
        if department.return_technic(technic):
            technic.dict = {technic.id: 1}
            self.take_technic(technic.dict)
    pass


class Technic:
    cur_id = 0
    def __init__(self, mark, model, format):
        self.mark = mark
        self.model = model
        self.format = format
        self.id = Technic.cur_id
        Technic.cur_id += 1
    pass


class Printer(Technic):
    def __init__(self, mark, model, format, type_printer, color): #type_printer - лазерный или чернильный, color - ч/б или цветной
        Technic.__init__(self, mark, model, format)
        self.type_printer = type_printer
        self.color = color
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


class Department():
    cur_id = 0
    def __init__(self, title):
        self.title = title
        self.cur_id = Department.cur_id
        self.orgtechnics = []
        Department.cur_id += 1

    def take_technic(self, technic):
        if len(self.orgtechnics) > 0:
            print('В отделе уже есть оргтехника!')
            return False
        else:
            self.orgtechnics.append(technic)
            return True

    def return_technic(self, technic):
        self.orgtechnics.append(technic)
        if technic in self.orgtechnics:
            self.orgtechnics.remove(technic)
            return True
        return False



print(Technic.cur_id)
xerox_1 = Xerox('Xerox', 'Versalink C505', 'A3', 'List')
xerox_2 = Xerox('Xerox', 'Versalink C505', 'A3', 'List')
xerox_3 = Xerox('Xerox', 'Versalink C505', 'A3', 'List')
xerox_4 = Xerox('Xerox', 'Versalink C505', 'A3', 'List')

printer_1 = Printer('HP', 'LaserJet 1020', 'A4', 'Laser', 'Black')
printer_2 = Printer('HP', 'LaserJet 1020', 'A3', 'Laser', 'Black')
printer_3 = Printer('HP', 'LaserJet 1020', 'A4', 'Laser', 'Black')
printer_4 = Printer('HP', 'LaserJet 1020', 'A3', 'Laser', 'Black')

scanner_1 = Scanner('HP', 'LaserJet', 'A3', 'Tablet', 'Black', '640x480')
scanner_2 = Scanner('Apple', 'Iphone 8', 'A4', 'Handle', 'Color', '800x600')
scanner_3 = Scanner('Iris', 'Book5', 'A4', 'Handle', 'Color', '1024x960')
scanner_4 = Scanner('Brother', 'DS640', 'A4', 'Mobile', 'Color', '1096x1080')

storage = Storage()

buh = Department('Бухгалтерия')
yur = Department('Юридический отдел')
contract_dep = Department('Отдел сопровождения договоров')
project = Department('Проектный офис')

print(Technic.cur_id)
print(printer_4.color)
print(printer_4.id)
print(contract_dep.cur_id)

print(contract_dep.orgtechnics)
contract_dep.take_technic(scanner_4)
print(contract_dep.orgtechnics)
contract_dep.take_technic(printer_3)

print(contract_dep)


storage.take_technic(scanner_4)
print(storage.technics)

storage.take_technic(scanner_4)
