#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('source.txt', 'r') as file_obj:
    content = file_obj.readlines()
    print(f'В файле {file_obj.name} всего {len(content)} строк:')
    for el in content:
        keywords = el.split(' ')
        print(f'в {content.index(el) + 1} строке {len(el)} символов и {len(keywords)} слов')