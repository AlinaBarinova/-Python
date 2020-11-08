check = True
count = 0
while check:
    user_numbers = input('Введите числа через пробел\n>>>')
    numbers = user_numbers.split(' ')
    for user_input in numbers:
        try:
            value = int(user_input)
            count += value
        except ValueError:
            if user_input.lower() == 'q':
                check = False
                break
            print('Введено неверное значение')
            break
    print(count)