user_input = input('Input number:')
user_number = int(user_input)
remain = user_number
rank = 0
max_number = 0
while remain != 0:
    remain = remain // 10
    if int(user_input[rank]) > max_number:
        max_number = int(user_input[rank])
    rank += 1
print('\n Maximum number in string:', max_number)
