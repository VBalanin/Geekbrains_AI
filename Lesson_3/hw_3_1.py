def divide(x, y):
    try:
        z = x / y
    except ZeroDivisionError:
        return
    return z


arg1 = float(input('Input dividend: '))
arg2 = float(input('Input divider: '))
print(divide(arg1, arg2))
