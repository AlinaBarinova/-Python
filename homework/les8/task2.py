class ZeroDivision(Exception):
    def __init__(self, err):
        self.err = err


if __name__ == '__main__':

    num1, num2 = float(input('Число 1 = ')), float(input('Число 2 = '))
    try:
        # result = num1 / num2
        if num2 == 0:
            raise ZeroDivision("Деление на 0")
    except ZeroDivision as e:
        print(e)
    else:
        print(f"Ответ = {num1 / num2}")