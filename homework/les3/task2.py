def user_info(name, lastname, birthday, city, email, phone):
    a = f"{name} {lastname}, {birthday}, {city}, {email}, {phone}"
    return a
print(user_info(
    name='Alina',
    lastname='Barinova',
    birthday='24.04.1994',
    city='Moscow',
    email='barinova.ai4@gmail.com',
    phone=89689283756))