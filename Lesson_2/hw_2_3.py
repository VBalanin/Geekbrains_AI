usr_str = input('Input number of current month:')
num = int(usr_str)
print(num)
print('Resolving with list:')
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if winter.count(num) > 0:
    print('Now is winter!')
elif spring.count(num) > 0:
    print('Now is spring!')
elif summer.count(num) > 0:
    print('Now is summer!')
elif autumn.count(num) > 0:
    print('Now is autumn!')
else:
    print('Are you from Earth?')
print('Resolving with dict:')
time_of_year = dict(winter=(12, 1, 2), spring=(3, 4, 5), summer=(6, 7, 8), autumn=(9, 10, 11))
for key in time_of_year.keys():
    s = time_of_year.get(key)
    if s.count(num) > 0:
        print('Now is', key)
