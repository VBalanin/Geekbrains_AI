class Date:
    def __init__(self, raw_date):
        self.date = raw_date

    @classmethod
    def split_date(cls, date):
        only_num = date.split('-')
        return int(only_num[0]), int(only_num[1]), int(only_num[2])

    @staticmethod
    def validator(day, month, year):
        if 1 <= day < 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return f'Date is correct'
                else:
                    return f'Wrong year'
            else:
                return f'Wrong month'
        else:
            return f'Wrong day'


data_for_val = Date.split_date('28-11-2020')
print(f'Введенные данные: {data_for_val}')
print(Date.validator(data_for_val[0], data_for_val[1], data_for_val[2]))

data_for_val = Date.split_date('32-11-2020')
print(f'Введенные данные: {data_for_val}')
print(Date.validator(data_for_val[0], data_for_val[1], data_for_val[2]))

day = Date('30-11-2020')
data_for_val = day.split_date(day.date)
print(f'Введенные данные: {data_for_val}')
print(Date.validator(data_for_val[0], data_for_val[1], data_for_val[2]))
