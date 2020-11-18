from sys import argv


def salary_calc(data):
    man_hour = float(data[1])
    rate = float(data[2])
    bonus = float(data[3])
    return man_hour * rate * (1+bonus / 100)


print(f"Your salary is - {salary_calc(argv)} USD")
