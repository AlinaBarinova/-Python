user_number = int(input('Введите любое целое положительное число\n>>>'))
a = user_number % 10
user_number = user_number // 10
while user_number > 0:
    if user_number % 10 > a:
        a = user_number % 10
    user_number //= 10
print(a)

