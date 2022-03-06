
from itertools import count

def int_generator(start_num, end_num):
    for el in count(start_num):
        if el > end_num:
            break
        else:
            print(el)
