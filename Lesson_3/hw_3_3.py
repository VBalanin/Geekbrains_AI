def my_func(a, b, c):
    args = [a, b, c]
    args.sort()
    return args[1] + args[2]


a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))
print(my_func(a, b, c))
