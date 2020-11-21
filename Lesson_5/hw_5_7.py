import json

in_file = open("hw_5_7.txt", 'r')
words = []
m_list = []
firm_list = {}
profit = {}
with in_file:
    for line in in_file:
        words = line.split(' ')
        words[3] = words[3].rstrip()
        margin = int(words[2]) - int(words[3])
        firm_list[words[0]] = margin
        if margin > 0:
            m_list.append(margin)
avr_profit = sum(m_list) / len(m_list)
profit['average_profit'] = avr_profit
m_list = [firm_list, profit]
print(m_list)
with open("hw_5_7.json", "w") as out_file:
    json.dump(m_list, out_file)
