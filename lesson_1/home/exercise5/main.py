revenue_str = input('Введите значение выручки: ')
cost_str = input('Введите значение издержек: ')
revenue = float(revenue_str)
cost = float(cost_str)

if revenue > cost:
    print('Фирма работала с прибылью')
    profit = (revenue - cost) / revenue
    print(f'Рентабельность составляет: {profit:.3f}')
    employees_str = input('Введите количество сотрудников: ')
    employees = float(employees_str)
    while employees < 1:
        employees_str = input('Фирма не может быть без сотрудников. Введите количество сотрудников: ')
        employees = float(employees_str)
    employ_profit = (revenue - cost) / employees
    print(f'Прибыль составляет: {employ_profit:.2f} у.е. на одного сотрудника')
elif revenue == cost:
        print('Фирма работала как все)')
else:
    print('Фирма работала с убытком')
