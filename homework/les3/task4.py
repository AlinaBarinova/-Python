def my_func1(x: int, y: int) -> float:
    a = x ** y
    return a

def my_func2(x: int, y: int) -> float:
    count = 1
    a = x
    while count != abs(y):
        x *= a
        count += 1
    return 1 / x

print(my_func1(5, -2))
print(my_func2(5, -2))
