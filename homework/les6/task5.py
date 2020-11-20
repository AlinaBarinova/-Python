class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self.title} : Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'{self.title} : Запуск отрисовки ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title} : Запуск отрисовки карандашом'


class Handle(Stationery):
    def draw(self):
        return f'{self.title}: Запуск отрисовки маркером'


stat = Stationery('stationery')
pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

print(stat.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())