# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

# решение на списках
seasons_list = ('Winter', 'Spring', 'Summer', 'Autumn')
months_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
month_str = input(f'Enter integer number from 1 to 12: ')
month = int(month_str)
#print(months_list)

for el_season in months_list:
    season_index = months_list.index(el_season) #запоминаем индекс внешнего списка
    season = months_list[season_index]
    for month_num in season:                    #проходим по элементам внутреннего списка
        if month_num == month:
            print(seasons_list[season_index])   #если находим нужное число выводим элемент списка времен года

# решение на словарях
winter = 'Winter'
spring = 'Spring'
summer = 'Summer'
autumn = 'Autumn'
month_seas_dict = {'12': winter, '1': winter, '2': winter, '3': spring, '4': spring, '5': spring, '6': summer, '7': summer, '8': summer, '9': autumn, '10': autumn, '11': autumn}
print(month_seas_dict[month_str])



