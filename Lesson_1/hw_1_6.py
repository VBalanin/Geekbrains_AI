bingo = False
day_count = 1
first_day_res = float(input("Input the first day result: "))
eligible_day_res = float(input("Input your eligible result: "))
if first_day_res > eligible_day_res:
    print('You reached it already!')
else:
    while not bingo:
        first_day_res = first_day_res * 1.1
        day_count += 1
        if first_day_res > eligible_day_res:
            bingo = True
print("You get the result on %d day!" % day_count)
