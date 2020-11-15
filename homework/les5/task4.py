words_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_output = open("file_task4_2.txt", "w", encoding='UTF-8')

with open("file_task4.txt", 'r', encoding='UTF-8') as open_file:
    for line in open_file:
        new_line = line.split(' - ')
        new_line[0] = words_dict[new_line[0]]
        new_line = ' - '.join(new_line)
        file_output.write(new_line)