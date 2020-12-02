class Not_Digit(Exception):
    def __init__(self, arg):
        self.txt = arg

    def check_digit(self):
        if self.txt.isnumeric():
            return True
        else:
            return False


buffer = []
out = ''
while True:
    try:
        data = input('Введите числа и нажмите Enter (q для выхода)) - ')
        digit_list = data.split()
        for i in digit_list:
            a = Not_Digit(i)
            if a.check_digit():
                buffer.append(int(i))
            else:
                out = i
                raise Not_Digit('Вы ввели не число')

    except Not_Digit as err:
        print(err)
        if out == 'q':
            break

print(buffer)
