class Error(Exception):
    def __init__(self, err=''):
        self.err = err


class InputList:
    print('Для остановки введите stop')
    inp_list = []

    def input(self):
        while True:
            a = input('Введите значение: ')
            if a.lower() == 'stop':
                break
            else:
                try:
                    float(a)
                except ValueError:
                    print('это не число')
                else:
                    self.inp_list.append(float(a))

        return self.inp_list


if __name__ == '__main__':
    ls = InputList()
    print(ls.input())