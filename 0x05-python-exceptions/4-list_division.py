#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    if list_length:
        new = []
        for i in range(list_length):
            try:
                c = my_list_1[i] / my_list_2[i]
            except (ZeroDivisionError, TypeError, IndexError as err):
                if (ZeroDivisionError):
                    print("division by 0")
                if (TypeError):
                    print("wrong type")
                if (IndexError):
                    print("out of range")
                c = 0
            finally:
                new.append(c)
        return (new)
    return ([])

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
