def my_func1(a, b):
    b = abs(b)
    res = 1 / a ** b
    return res


def my_func2(a, b):
    b = abs(b)
    for i in range(b - 1):
        a *= a
    res = 1 / a
    return res


a = int(input("Input positive number: "))
b = int(input("Input negative number: "))

print(my_func1(a, b))
print(my_func2(a, b))
