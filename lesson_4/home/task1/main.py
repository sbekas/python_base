# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

work_time = int(argv[1])
rate = int(argv[2])
premium = int(argv[3])
salary = work_time * rate + premium
print(salary)