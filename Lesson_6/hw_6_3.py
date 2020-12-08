class Worker:
    def __init__(self, name, surname, position, income=None):
        if income is None:
            income = {}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def print_usr_data(self):
        print(f"Имя - {self.name} , Фамилия - {self.surname}, Должность - {self.position}.")
        print(self._income)


class Position(Worker):

    def get_full_name(self):
        full_name = f"{self.name} {self.surname}"
        return full_name

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        return total_income


usr_data = ['Иван', 'Иванов', 'директор']
usr_income = {"wage": 1000, "bonus": 500}
usr_data2 = ['Петр', 'Петров', 'инженер']
usr_income2 = {"wage": 300, "bonus": 180}
user = Position(*usr_data, usr_income)
user2 = Position(*usr_data2, usr_income2)
print(f"Сотрудник: {user.get_full_name()}, c общим доходом: {user.get_total_income()}")
print(f"Сотрудник: {user2.get_full_name()}, c общим доходом: {user2.get_total_income()}")


