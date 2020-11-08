def asking(text: str, check=False) -> int:

    while True:
        user_input = input(text)
        try:
            user_number = int(user_input)
        except ValueError as error:
            if user_input.lower() == 'q':
                return
            print('Введено неверное значение')
            continue
        if check and user_number == 0:
            print('Введено неверное значение')
            continue
        return user_number


def div(a: float, b: float) -> float:
    result = a / b
    return result


while True:
    num_1 = asking('Введите первое число\n>>> ')
    if num_1 is None:
        break
    num_2 = asking('Введите второе число\n>>> ', True)
    if num_2 is None:
        break
    print(div(num_1, num_2), '\n')

