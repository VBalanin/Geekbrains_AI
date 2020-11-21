import os
if os.path.exists("hw_5_1.txt"):
    test_file = open("hw_5_1.txt", 'a')
else:
    test_file = open("hw_5_1.txt", 'w')
user_data = 'base'
while user_data:
    user_data = input("Input string or Enter for exit: ")
    test_file.writelines(user_data)
    test_file.writelines('\n')

test_file.close()
