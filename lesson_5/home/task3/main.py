# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

with open('personal.txt', 'r') as file_obj:
    content = file_obj.readlines()
#    print(content)
    dict = {}
    min_salary = {}
    for el in content:
        personal = el.split(': ')
        dict.update({personal[0]:int(personal[1])})

    com = 0
    for key, value in dict.items():
        com += value
        if value < 20000:
            min_salary.update({key: value})

    print('Сотрудники с окладом менее 20000:')
    for key, value in min_salary.items():
        print(f'{key}')
    print(f'Средний оклад составляет: {com/len(dict):.2f}')
