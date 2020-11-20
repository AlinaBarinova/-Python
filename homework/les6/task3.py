class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print('ФИО: ', end=' ')
        return self.name.title() + ' ' + self.surname.title()

    def get_total_income(self):
        print('Доход сотрудника:', end=' ')
        return sum(self._income.values())


pos = Position('петя', 'петров', 'Специалист', 80000, 20000)
print(pos.get_full_name())
print(pos.get_total_income())
print(pos.name, pos.surname, pos.position, pos._income)