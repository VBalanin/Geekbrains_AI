words = []
my_dict = {}
key = ''
value = 0

in_file = open("hw_5_6.txt", 'r')
with in_file:
    for line in in_file:
        words = line.split(' ')
        key = words[0]
        key = key[:len(key) - 1]
        summary = []
        for i in range(1, len(words)):
            digit = ''
            for j in words[i]:
                if '0' <= j <= '9':
                    digit += j
            if digit != '':
                summary.append(int(digit))
        value = sum(summary)
        my_dict[key] = value
print(my_dict)
