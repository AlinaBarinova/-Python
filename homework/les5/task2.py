cnt_lines, cnt_words = 0, []
with open('file_task2.txt', 'r', encoding='UTF-8') as open_file:
    for line in open_file:
        cnt_lines += 1
        cnt_words.append(line.count(' ') + 1)

print(f"Количество строк = {cnt_lines}")
for num, cnt in enumerate(cnt_words):
    print(f"Строка: {num+1:2} Слов: {cnt:2}")