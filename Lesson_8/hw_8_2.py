class Div_by_Null(Exception):
    def __init__(self, err_value):
        self.err_value = str(err_value)


a = int(input('Введите делимое - '))
b = int(input('Введите делитель - '))
try:
    if b == 0:
        raise Div_by_Null('Вы пытаетесь поделить на 0')
except Div_by_Null as err:
    print(err)
else:
    print(f'Результат деления - {a / b}')
