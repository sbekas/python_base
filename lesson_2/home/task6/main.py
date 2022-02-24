# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

#features_list = ['название', 'цена', 'количество', 'ед']
features_list = []
#print(features_list)
# формируем список характеристик товара
features_list_el = '1'

while features_list_el != '':
    features_list_el = input('Введите новую харакетристику товара или нажмите Enter для отмены: ')
    if features_list_el == '':
        break
    else:
        features_list.append(features_list_el)

print(features_list)

goods_list = list()                         # список товаров с характеристиками
features_numbers = len(features_list)       # количество характеристик
current_good = dict()                       # формируем структуру кортежа товара

# формируем карточки товаров
current_good = dict()
print(features_numbers)
input_field = '1'
good_pos = 1
while input_field != '':
    print(f'Заполняем карточку товара {good_pos}, для завершения нажмите Enter')
    for el in features_list:
        if input_field == '':
            break
        input_field = input(f'Введите "{el}": ')
        current_good[el] = input_field
    print(current_good)
    if input_field != '':
        new_good = current_good.copy()
        goods_list.append((good_pos, new_good))
#        print(goods_list)
    good_pos += 1

# формируем структуру анализир. данных
for el in features_list:
        current_good[el] = []
#print(current_good)

# создаем результирующий список
for i, curr_good in goods_list:
    for key, value in curr_good.items():
        current_good[key].append(value)
print(current_good)