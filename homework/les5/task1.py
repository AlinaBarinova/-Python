with open('text_file.txt', 'w', encoding='utf-8') as file:
    text = ''
    print('Введите данные')
    while True:
        str = input('>>> ')
        if str:
            text += f'{str}\n'
        else:
            break
    print(text, file=file)

