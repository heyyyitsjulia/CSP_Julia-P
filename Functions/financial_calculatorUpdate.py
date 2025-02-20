# Julia Properzi, Financial Calculator Update python
def info(cost, income, type):
    percent = cost/income *100
    print(f"Your {type} is ${cost:.2f} which is {percent}% of your income.")

# print statment that welcomes user and tells what program does
welcome = input("Welcome! This will create a personal finance calculator and will help you figure out how much you need to put into savings, based off your income and expenses.")
# ask what their income is (variable an input)
income = float(input("What is your monthly income?(don't use commas)\n"))
# ask what their rent is (variable an input)
rent = float(input("What is your monthly rent?\n"))
# ask what their utilities is (variable an input)
utilities = float(input("What is the cost of your utilities? every month\n"))
# ask what their groceries is (variable an input)
groceries = float(input("What is the average cost of your groceries?\n"))
# ask what their transportation is (variable an input)
transportation = float(input("How much does it cost for your transportation?\n"))
# calculate savings as 10% of income (income*.1) (variable)
savings = income*.1
# calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
spendings = income-savings-rent-utilities-groceries-transportation

info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spendings, income, "spendings")