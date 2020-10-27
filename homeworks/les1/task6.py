day = 1
a = int(input('Результат в первый день\n>>>'))
b = int(input('Целевой результат\n>>>'))
while a < b:
    print(a)
    a = a + (a * 0.1)
    day = day + 1
print(day)



