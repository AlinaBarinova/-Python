my_list = [7, 5, 3, 3, 2]
user_number = int(input("Введите число\n>>>"))
for el in my_list:
    if user_number > el:
        my_list.insert(my_list.index(el), user_number)
    elif user_number == el:
        my_list.insert((my_list.index(el) + my_list.count(el)), user_number)
    elif user_number < el: continue
    break
else:
    my_list.append(user_number)
print(my_list)
