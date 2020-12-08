def int_func(var):
    cap = var.title()
    return cap


var = input('Input word: ')
if var.find(' ') != -1:
    z = var.find(' ')
    var = var[:z]
print(int_func(var))
var = input('Input sentence: ')
print(int_func(var))
