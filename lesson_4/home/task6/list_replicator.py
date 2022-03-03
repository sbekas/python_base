
from itertools import cycle

def replicator(source_list):
    copy_list = []
    c = 0
    list_last_el_num = len(source_list)
    for el in cycle(source_list):
        if c == list_last_el_num:
            break
        copy_list.append(el)
        c += 1
    return copy_list
