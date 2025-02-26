# Julia Properzi, Financial Calculator Update python
def values(type):
    return int(input(f"How much is your {type}:\n"))

def info(cost, income, type):
    percent = cost/income *100
    print(f"Your {type} is ${cost:.2f} which is {percent}% of your income.")

income = values("income")
rent = values("Rent")
utilities = values("utilities")
groceries = values("groceries")
transportation = values("transportation")

savings = income * .1
spendings = utilities + groceries+ transportation + rent

info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spendings, income, "spendings")