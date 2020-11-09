some_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [el for el in some_list if some_list.count(el) == 1]
print(result)