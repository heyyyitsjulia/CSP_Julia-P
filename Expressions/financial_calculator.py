# Julia Properzi, Financial Calculator python

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
# calculate percent income of rent (rent/income *100) (variable)
percent_rent = rent/income *100
# calculate percent income of utilites (utilities/income *100) (variable)
percent_utilities = utilities/income *100
# calculate percent income of groceries (groceries/income *100) (variable)
percent_groceries = groceries/income *100
# calculate percent income of transportation (transportation/income *100) (variable)
percent_transportation = transportation/income *100
# calculate percent income of spending (spending/income *100) (variable)
percent_spending = spendings/income *100
# Your rent is $XX.XX which is XX% of your income. (Print)
print(f"your rent is {rent} which is {percent_rent: .2f} percent of your income")
# Your utlities is $XX.XX which is XX% of your income. (Print)
print(f"The utilities cost is {utilities} which is {percent_utilities: .2f} percent of your income")
# Your groceries is $XX.XX which is XX% of your income. (Print)
print(f"The cost of your groceries is {groceries} which is {percent_groceries: .2f} percent of your income")
# Your transportation is $XX.XX which is XX% of your income. (Print)
print(f"The cost of your transportation is {transportation} which is {percent_transportation: .2f} percent of your income")
# Your savings is $XX.XX which is XX% of your income. (Print)
print(f"Your savings is {savings} which is {percent_spending: .2f} percent of your income")
# Your spending is $XX.XX which is XX% of your income. (Print)
print(f"Your spendings is {spendings} which is {percent_spending: .2f} percent of your income")