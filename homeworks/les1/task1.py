variable_str1 = 'Продолжение'
variable_str2 = 'следует'
variable_str3 = variable_str1 + ' ' + variable_str2 + '...'
print(variable_str3)

variable_int = 954
print(variable_int/6)

variable_float = 45.5
print(100*variable_float)
print((variable_int-variable_float)//30)

user_surname = input('Ваша фамилия\n>>>')
user_name = input('Ваше имя\n>>>')
user_middle_name = input('Ваше отчество\n>>>')
birthday = input('Ваша дата рождения\n>>>')
country = input('Страна проживания\n>>>')
city = input('Город проживания\n>>>')
count_courses = input('Количество пройденных курсов\n>>>')
actual_course = int(count_courses)+1
greeting = f"Добрый день, меня зовут {user_surname} {user_name} {user_middle_name} , я родилась(-ся) {birthday}, в настоящий момент пpоживаю в {country}, {city} и это мой {actual_course} курс."
print(greeting)
print('Добрый день, меня зовут {0} {1} {2} , я родилась(-ся) {3}, в настоящий момент пpоживаю в {4}, {5} и это мой {6} курс.'.format(user_surname,user_name,user_middle_name,birthday,country,city,actual_course))


