"""
Если желаете использовать функцию из этого списка, надо написать ее аналог
sum()
map()
reduce()
min()
max()
enumerate()
zip()
print()
"""

def my_sum(a: int, b: int) -> int:
    """
    My sum func for two elements
    :param a int or float digit
    :param b int or float digit
    :return sum a b
    """
    result = a + b
    return result

def some (a: int) -> int:
    return a ** 3

def my_map(funk, iter_obj):
    result = []
    for itm in iter_obj:
        result.append(funk(itm))
        return

 # функция генератор -> yield
# если преобразование данных из ввода, то обязательно try, except