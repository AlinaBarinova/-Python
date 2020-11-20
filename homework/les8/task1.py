from datetime import date


class Data:
    def __init__(self, data: str):
        self.data = data

    @classmethod
    def data_numb(cls, data):
        data_as_num = [int(n) for n in data.replace(' ', '').split('-')]
        return data_as_num[0], data_as_num[1], data_as_num[2]

    @staticmethod
    def validation(data):
        data_as_num = [int(n) for n in data.replace(' ', '').split('-')]
        try:
            _ = date(data_as_num[2], data_as_num[1], data_as_num[0])
            return f"Все ок"
        except ValueError:
            return f"Ошибка во входных данных"


if __name__ == '__main__':
    print(Data.data_numb('25-06-2020'))

    print(Data.validation('30-02-2020'))
    print(Data.validation('29-02-2020'))