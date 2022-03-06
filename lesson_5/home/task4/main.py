# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
out_list = []
with open('source.txt', 'r') as file_obj:
    content = file_obj.readlines()
    for el in content:
        pair = el.split(' - ')
        num_letters = pair[0]
#        print(num_letters)
        new_line = str(dict.get(num_letters)) + ' - ' + pair[1]
        out_list.append(new_line)
    print(out_list)

with open('out.txt', 'w') as file_obj:
    for el in out_list:
        file_obj.write(el)




