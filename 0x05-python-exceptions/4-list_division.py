#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    for i in range(list_length):
        try:
            item = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print("division by 0")
            item = 0
        except (IndexError):
            print("out of range")
            item = 0
        except (TypeError, ValueError):
            print("wrong type")
            item = 0
        finally:
            div.append(item)
    return div
