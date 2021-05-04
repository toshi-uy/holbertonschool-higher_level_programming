#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        res_tuple = ()
        lists = []
        if len(tuple_a) > 1 and len(tuple_b) > 1:
                res_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
                return res_tuple
        else:
                for i in range(0, 2):
                        if len(tuple_a) >= 1 and i < len(tuple_a):
                                lists.append(tuple_a[i])
                        else:
                                lists.append(0)
                        if len(tuple_b) >= 1 and i < len(tuple_b):
                                lists.append(tuple_b[i])
                        else:
                                lists.append(0)
                res_tuple = (lists[0] + lists[1], lists[2] + lists[3])
                return res_tuple
