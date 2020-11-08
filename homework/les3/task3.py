def my_func(arg1: int, arg2: int, arg3: int) -> int:
    a = min(arg1, arg2, arg3)
    result = arg1 + arg2 + arg3 - a
    return result

print(my_func(arg1 = 80, arg2 = 87, arg3 = 76))
