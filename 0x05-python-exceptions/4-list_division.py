#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    if list_length:
        new = []
        for i in range(list_length):
            try:
                c = my_list_1[i] / my_list_2[i]
            except Exception as err:
                if isinstance(err, ZeroDivisionError):
                    print("division by 0")
                elif isinstance(err, TypeError):
                    print("wrong type")
                elif isinstance(err, IndexError):
                    print("out of range")
                c = 0
            finally:
                new.append(c)
        return (new)
    return ([])
