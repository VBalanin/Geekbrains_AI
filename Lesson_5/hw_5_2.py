count_line = 0
count_words = 0
words = []
with open("hw_5_2.txt") as f_obj:
    for line in f_obj:
        count_line += 1
        words = line.split(' ')
        count_words += len(words)
print(f"There are {count_line} strings and {count_words} words")
