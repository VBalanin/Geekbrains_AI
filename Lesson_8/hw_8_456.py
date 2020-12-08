class Warehouse:
    _capacity = 100
    storage = []

    def __init__(self, **kwargs):
        self.add_data = kwargs

    @staticmethod
    def fulfill():
        try:
            print('Введите тип устройства: p(Принтер), s(Сканнер), с(Копир)')
            unit_t = input(f'--> ')
            print('Введите модель: ')
            unit_m = input(f'--> ')
            print('Введите количество: ')
            unit_q = int(input(f'--> '))
            print('Введите цену: ')
            unit_p = float(input(f'--> '))
            print('Введите размер для хранения единицы продукции: ')
            unit_s = int(input(f'--> '))
            print('Введите ответственного или оставьте пустым (склад): ')
            unit_o = input(f'--> ')
            if unit_o == '':
                unit_o = 'склад'
            if unit_t == 'p':
                unit = Printer(unit_m, unit_q, unit_p, unit_s, unit_o)
                unit.characteristics()
                Warehouse._capacity -= unit_q * unit_s
                Warehouse.storage.append(unit)
            elif unit_t == 's':
                unit = Scanner(unit_m, unit_q, unit_p, unit_s, unit_o)
                unit.characteristics()
                Warehouse._capacity -= unit_q * unit_s
                Warehouse.storage.append(unit)
            elif unit_t == 'c':
                unit = Copier(unit_m, unit_q, unit_p, unit_s, unit_o)
                unit.characteristics()
                Warehouse._capacity -= unit_q * unit_s
                Warehouse.storage.append(unit)
            else:
                raise ValueError
        except:
            print('Ошибка ввода данных!')
            return f'Ошибка'
        else:
            print(f'Для выхода введите "Q", для продолжения "Enter"')
            q = input('--> ')
            if a == 'Q' or q == 'q':
                return f'Exit'
            else:
                return Warehouse.fulfill()

    @property
    def capacity(self):
        return f' {self._capacity}'

    @staticmethod
    def warehouse_state():
        count = 1
        for item in Warehouse.storage:
            print(f'{count}: {item}')
            count += 1


class Office_Equipment:
    def __init__(self, model, quantity, price, size, owner='Склад'):
        self.model = model
        self.quantity = quantity
        self.price = price
        self.size = size
        self.owner = owner


class Printer(Office_Equipment):
    def __init__(self, model, quantity, price, size, owner):
        super().__init__(model, quantity, price, size, owner)
        self.datasheet = ()
        self.kind = self.__class__.__name__
        self.unit_description = {'Модель': self.model, 'Количество': self.quantity, 'Цена': self.price,
                                 'Отв.': self.owner, 'Характеристики': self.datasheet}

    def characteristics(self):
        print(f'Введите через запятую харктеристики для {self.model} в формате характеристика: значение \n или '
              f'оставьте поле пустым (Enter):')
        data = input(f'--> ')
        self.datasheet = data.split(', ')
        print(self.datasheet)

    def __str__(self):
        return f'{self.unit_description}'


class Scanner(Office_Equipment):
    def __init__(self, model, quantity, price, size, owner):
        super().__init__(model, quantity, price, size, owner)
        self.datasheet = ()
        self.kind = self.__class__.__name__
        self.unit_description = {'Модель': self.model, 'Количество': self.quantity, 'Цена': self.price,
                                 'Отв.': self.owner, 'Характеристики': self.datasheet}

    def characteristics(self):
        print(f'Введите через запятую харктеристики для {self.model} в формате характеристика: значение \n или '
              f'оставьте поле пустым (Enter):')
        data = input(f'--> ')
        self.datasheet = data.split(', ')
        print(self.datasheet)

    def __str__(self):
        return f'{self.unit_description}'


class Copier(Office_Equipment):
    def __init__(self, model, quantity, price, size, owner):
        super().__init__(model, quantity, price, size, owner)
        self.datasheet = ()
        self.kind = self.__class__.__name__
        self.unit_description = {'Модель': self.model, 'Количество': self.quantity, 'Цена': self.price,
                                 'Отв.': self.owner, 'Характеристики': self.datasheet}

    def characteristics(self):
        print(f'Введите через запятую харктеристики для {self.model} в формате характеристика: значение \n или '
              f'оставьте поле пустым (Enter):')
        data = input(f'--> ')
        self.datasheet = data.split(', ')
        print(self.datasheet)

    def __str__(self):
        return f'{self.unit_description}'


a = Warehouse()
a.fulfill()
a.warehouse_state()
print(f'Осталось места для хранения - {a.capacity}')
