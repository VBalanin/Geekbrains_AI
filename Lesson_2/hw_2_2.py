usr_str = input('Input any values with space as separator:')
usr_list = usr_str.split()
length_list = len(usr_list)
sort_list = []
i = 0
if length_list % 2 == 0:
    while i < length_list - 1:
        sort_list.append(usr_list[i + 1])
        sort_list.append(usr_list[i])
        i += 2
elif length_list <= 1:
    print('Too short input')
    sort_list.extend(usr_list)
else:
    while i < length_list - 1:
        sort_list.append(usr_list[i + 1])
        sort_list.append(usr_list[i])
        i += 2
        if i == length_list - 1:
            sort_list.append(usr_list[i])
print('Sorted list:')
print(sort_list)
