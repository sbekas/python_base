#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(keyword):
    mod_key = keyword.title()
    return mod_key


out_str = ''
text = input('Введите текст (латинские буквы в нижнем регистре, через пробел): ')
text_list = text.split(' ')
print(text_list)
for el in text_list:
    modif_key = int_func(el)
    out_str += modif_key + ' '
print(out_str)
out_str_mod = out_str[:-1:] #убираем последний пробел
print(out_str_mod)
