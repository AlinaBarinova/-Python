def sum_numbers(new_line):
    st_with_num = ''
    for ch in range(len(new_line)):
        if new_line[ch].isdigit():
            st_with_num += new_line[ch]
            if not new_line[ch + 1].isdigit():
                st_with_num += ' '
    return sum([int(x) for x in st_with_num.split()])


dict_ans = {}
with open("file_task6.txt", "r", encoding='UTF-8') as open_file:
    for line in open_file:
        dict_ans[line[:line.find(':')]] = sum_numbers(line)

print(dict_ans)