salary_data = []
words = []
with open("hw_5_3.txt") as f_obj:
    print("Best salary has: ")
    for line in f_obj:
        words = line.split(' - ')
        for i in words:
            i = i.rstrip()
            if i.isdigit():
                salary = int(i)
                salary_data.append(salary)
                if salary > 20000:
                    print(words[0])
print(f"Middle level of salary is {sum(salary_data)/len(salary_data)}")
