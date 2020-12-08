def add(args):
    summa = 0
    for i in args:
        summa += int(i)
    return summa


buffer = 0
data = []
while True:
    usr_input = input("Input number with space and press Enter. For exit press 'q'.\n")
    if usr_input.find('q') == -1:
        data = usr_input.split(' ')
        buffer += add(data)
        print(buffer)
    else:
        cut = (usr_input.find('q'))
        usr_input = usr_input[:cut - 1]
        data = usr_input.split(' ')
        buffer += add(data)
        print(buffer)
        break
