import os
import random

usr_input = int(input('Введите любое число: '))
words = []
if os.path.exists("hw_5_5.txt"):
    out_file = open("hw_5_5.txt", 'w')
else:
    out_file = open("hw_5_5.txt", 'x')
with out_file:
    for i in range(1, usr_input + 1):
        out_file.write(str(random.randint(1, 100)))
        if i < usr_input:
            out_file.write(' ')
out_file = open("hw_5_5.txt")
line = out_file.readline()
words = line.split(' ')
number = [int(item) for item in words]
print(f"Сумма чисел в файле: {sum(number)}")
out_file.close()
