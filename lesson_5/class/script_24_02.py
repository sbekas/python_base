# with open('test.txt', 'rt') as file_obj:
#     #content = file_obj.read(20)
#     # content = file_obj.readline() # Hello world!\n
#     # print(content)
#     # content = file_obj.readline()
#     content = file_obj.readlines(0)
#     print(type(content))

# with open('result2.txt', 'wb') as file_obj:
#     content = [b'Hello world!265\n345435345435\n]
#     file_obj.write(content)

# with open('test.txt','rt') as file_obj:
#     print(file_obj.tell())
#     print(file_obj.tell())
#     content = file_obj.read()
#     print(content)
#     file_obj.seek(0)

# with open('result2.txt', 'a+') as file_obj:
#         file_obj.seek(5)
#         content = file_obj.read()
#         file_obj.write('Test STR\n')
#         print(content)

# with open('result2.txt', 'a+') as file_obj:
#     file_obj.seek(5)
#     #content = file_obj.read()
#     file_obj.write('Test STR\n')
#     print('Test STRrrrrrrrrrrrrr\n', file=file_obj)
#
# import os
#
# #os.rename('result.txt', 'result_new.txt')
# print(os.listdir())
# #print(os.remove('result2.txt'))
# # print(os.path.split('C:/Geek Brains/python_base/lesson_5/class/test.txt'))
# print(os.path.join('user', 'local', 'var', 'script'))

import json

# test_dict = {
#     'name': 'Damir',
#     'languages': ['Russian', 'English', 'Tatarcha'],
#     'age': 25
# }

# with open('test.txt', 'w') as file_obj:
#     json.dump(test_dict, file_obj)

# with open('test.txt', 'w') as file_obj:
#      content = json.load(file_obj)
#      print(content)
#
#    json.dump(conten, file_obj)

# import shutil
#
# shutil.move('result1_copy.txt','result1_copy2.txt')


import sys
print(sys.path)

print(sys.executable)
sys.exit(78)