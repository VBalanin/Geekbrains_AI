proceeds = int(input("Input proceeds your company:"))
costs = int(input("Input expenses your company:"))
profit = proceeds - costs
if profit > 0:
    print("Congratulation, finance result is good\n")
    print("Your profitability is: {:.2%}" .format(profit / costs))
    number_emp = int(input("input number of yours employees:"))
    print("Your profitability for one employee: {:.2f}".format(profit / number_emp))
elif profit == 0:
    print("Nice try")
else:
    print("You must think about yours business methods")
