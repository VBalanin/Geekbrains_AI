my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
length = len(my_list)
new_list = [my_list[i] for i in range(length) if my_list.count(my_list[i]) == 1]
print(new_list)
