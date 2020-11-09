some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [el for idx, el in enumerate(some_list[1:]) if el > some_list[idx]]

print(result)