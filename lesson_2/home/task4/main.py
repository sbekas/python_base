# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
string = input('Введите строку: ')
print(string)

string_split = string.split(' ')
#print(type(string_split))
for keyword in string_split:
    print(f'{string_split.index(keyword)}:{keyword[:10]}')
