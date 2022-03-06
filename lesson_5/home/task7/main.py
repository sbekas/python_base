# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json


def average(my_dict):
    result_dict = {}
    num = 0
    sum = 0
    average_sum = 0
    for key, value in my_dict.items():
        if value > 0:
           sum += value
           num += 1
    average_sum = sum / num
    result_dict["average_profit"] = average_sum
    return result_dict


with open('source.txt', 'r', encoding='UTF-8-sig') as file_obj: #без указания кодировки лезут строковые спецсимволы

    profit_firms_dict = {}
    average_profit_dict = {}
    content = file_obj.readlines()
    print(content)
    for el in content:
        firm = el.split(' ')[0]
        form = el.split(' ')[1]
        revenue = float(el.split(' ')[2])
        cost = float(el.split(' ')[3])
        profit = revenue - cost
        profit_firms_dict[firm] = profit
        firm_list = [profit_firms_dict, average(profit_firms_dict)]
    # print(profit_firms_dict)
    print(firm_list)

with open("out_file.json", "w") as write_f:
    json.dump(firm_list, write_f)
