#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def string_to_sum(text):
    num_list = text.split(' ')
#    print(num_list)
    result = 0
    for num_str in num_list:
        num = float(num_str)
        result += num
    return float(result)

with open('source.txt', 'w') as file_obj:
        input_str = input('Введите строку чисел, разделенных пробелом ("C" - остановить ввод): ')
        file_obj.write(input_str)

with open('source.txt', 'r') as file_obj:
        file_string = file_obj.readline()

print(f'Сумма чисел из файла {file_obj.name} равна {string_to_sum(file_string)}')