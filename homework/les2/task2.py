list_2 = [ ]
list_2.append(input("Введите первый элемент списка\n>>"))
list_2.append(input("Введите второй элемент списка\n>>"))
list_2.append(input("Введите третий элемент списка\n>>"))
list_2.append(input("Введите четвертый элемент списка\n>>"))
list_2.append(input("Введите пятый элемент списка\n>>"))
list_2.append(input("Введите шестой элемент списка\n>>"))
list_2.append(input("Введите седьмой элемент списка\n>>"))
print(list_2)
list_2[0], list_2[1] = list_2[0], list_2[1]
print(list_2[0], list_2[1])
list_2[0], list_2[1] = list_2[1], list_2[0]
print(list_2[0], list_2[1])
list_2[2], list_2[3] = list_2[2], list_2[3]
print(list_2[2], list_2[3])
list_2[2], list_2[3] = list_2[3], list_2[2]
print(list_2[2], list_2[3])
list_2[4], list_2[5] = list_2[4], list_2[5]
print(list_2[4], list_2[5])
list_2[4], list_2[5] = list_2[5], list_2[4]
print(list_2[4], list_2[5])
print(list_2)

