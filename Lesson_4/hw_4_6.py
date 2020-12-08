from itertools import count, cycle

start = int(input('Input any integer: '))
print('Next - Enter, exit - q + Enter')
x = count(start)
while input() != 'q':
    print(next(x))

start = input('Input any string: ')
m = start.split(' ')
x = cycle(m)
while input() != 'q':
    print(next(x))
