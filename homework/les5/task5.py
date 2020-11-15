from random import randint

file_to_inp = open("file_task5.txt", "w", encoding='UTF-8')

sequence = [randint(-100, 100) for _ in range(randint(4, 15))]
for x in sequence:
    file_to_inp.write(str(x)+' ')
file_to_inp.close()

with open("file_task5.txt", "r", encoding='UTF-8') as open_file:
    new_str = [int(x) for x in open_file.read().split()]

print(f"Сумма чисел = {sum(new_str)}")