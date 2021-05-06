#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list2 = my_list.copy()
    for i in range(len(my_list2)):
        if my_list2[i] == search:
            my_list2.remove(my_list[i])
            my_list2.insert(i, replace)
    return my_list2
