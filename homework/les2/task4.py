user_str = input("Введите строку из нескольких слов\n>>>")
user_str_list = user_str.split(' ')
print(user_str_list)
for ind, el in enumerate(user_str_list, 1):
    print(ind, el[:10])
