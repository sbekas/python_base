# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


# определение суммы элементов в списке
def sum_list_elements(source_list):
    sum = 0
    for el in source_list:
        el_int = int(el)
        sum += el_int
    return sum

# определение чисел в строке
def numbers_in_string(str):
    arg_list = list(str)
    last_sym_index = len(arg_list) - 1
    numbers_list = []
    curr_num = []
    # print(arg_list)
    for el in arg_list:
        if '0' <= el <= '9':
            # print(el)
            curr_num.append(el)
            if arg_list.index(el) == last_sym_index:# если последний символ цифра, то работает эта конструкция (костыль из-за последнего "\n")
                string_num = ''.join(curr_num)
                numbers_list.append(string_num)
                curr_num = []
        else:
            if len(curr_num) != 0:
                string_num = ''.join(curr_num)
                numbers_list.append(string_num)
                curr_num = []

    return sum_list_elements(numbers_list)

# основная функция: переформатирует строку в словарь
def string_to_dict(str):
    subject = str.split(':')[0]
    hours = str.split(':')[1]
    sum_hours = numbers_in_string(hours)
    dict[subject] = sum_hours
    return dict

with open('source.txt', 'r', encoding='UTF-8-sig') as file_obj: #без указания кодировки лезут строковые спецсимволы
    dict = {}
    content = file_obj.readlines()
    print(content)
    for el in content:
        string_to_dict(el)

print(dict)
