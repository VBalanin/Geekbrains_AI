usr_str = input('Input your data:')
usr_list = usr_str.split()
for nm, word in enumerate(usr_list, 1):
    print(nm, word[:10])
