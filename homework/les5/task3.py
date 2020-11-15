cnt, summ = 0, 0
print('Сотрудники с окладом < 20 тыс.:')

with open("file_task3.txt", 'r', encoding='UTF-8') as open_file:
    for line in open_file:
        new_line = line.split()
        cnt += 1
        summ += float(new_line[1])
        if float(new_line[1]) < 20000:
            print(new_line[0])

print(f"Средняя величина дохода = {summ/cnt:.2f}")