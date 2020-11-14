def user_data_output(**kwargs):
    s = []
    for key, values in kwargs.items():
        s.append(key)
        s.append(':')
        s.append(values)
        s.append(', ')
    o = ''.join(s)
    o = o[:-2]
    print(o)


db = []
usr = {}
print('Input user personal data')
count = 1
continuous = True
while continuous:
    usr['name'] = input('Input user name:')
    usr['family'] = input('Input user family:')
    usr['y_of_b'] = input('Input year of birthday:')
    usr['city'] = input('Input city:')
    usr['email'] = input('Input email:')
    usr['phone'] = input('Input phone:')
    usr_input = input("Enough?( y or n): ")
    if usr_input == 'y':
        usr_info = (usr.copy())
        db.append(usr_info)
        continuous = False
    else:
        usr_info = (usr.copy())
        db.append(usr_info)
        print("Next user:")

for usr_data in db:
    user_data_output(**usr_data)
