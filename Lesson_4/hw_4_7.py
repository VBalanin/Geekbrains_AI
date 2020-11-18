def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


n = int(input('Input number: '))
for el in fact(n):
    print(el)
