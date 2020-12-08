import os

words = []
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
in_file = open("hw_5_4_eng.txt")
if os.path.exists("hw_5_4_rus.txt"):
    out_file = open("hw_5_4_rus.txt", 'w')
else:
    out_file = open("hw_5_4_rus.txt", 'x')
with in_file, out_file:
    for line in in_file:
        words = line.split(' ')
        words[0] = translate.get(words[0])
        line = ' '.join(words)
        out_file.write(line)
