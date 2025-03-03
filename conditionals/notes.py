#Julia Properzi, Conditionals notes Python
name = input("What is your name?:\n")
#What puts something inside of the “if” statement? Having a tab thats right in front of the print statement.
if name == "LaRose":
    print("Hi Ms. LaRose")
else: # This happens if the condition is false.
    print(f"Hello {name}!")
# ^ the tab thats right here.

#What do if statements do? Checks a condition and if it is true it will do a thing.
if name == "LaRose": #<= this is the condition
    print("Hi Ms. LaRose")#<= This is what it does if true.

#What are boolean statements? A true or false statement. Part of the conditional that is either true or false.
if name == "LaRose": # <= This is the boolean statement it is either true or false.
    print("Hi Ms. LaRose")
else: # This happens if the condition is false.
    print(f"Hello {name}!")

#What do else statements do?
if name == "LaRose": 
    print("Hi Ms. LaRose")
else: # If the boolean is false, the else statement happens
    print(f"Hello {name}!")

#What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("How many cookies are there?\n"))
#computers read top to bottom, check the least likely first, more specific up top less specific goes lower.
if num == 0: # <= If always starts the conditional
    print("There are none.")
elif num ==1: # <= everything in between should be elif
    print("There is one.")
elif num < 4:
    print("There are a couple.")
elif num < 10:
    print("There are a few.")
else: #<= else always ends the conditional
    print("There are many.")

#What do each of the different symbols mean in conditionals?
#< Less than
#> Greater than
#<= Less than or equal to
#>= Greater than or equal to
#== Equal to (One equals sets a variable, two makes it equal to)
#=== *Doesn't exist in python
#! Not

#What are the 3 logical operators?
if num < 10 and num > 5: # and means both booleans must be true.
    print("This is a big single digit number")
elif num < 10 or num > 5: # or means one must be true
    print("This is a big single digit number")
elif not num < 10:  # not changes to check if false
    print("This is not a single digit number")

#What are logical operators for? Allows the code to handle more difficult questions... increases complexity.

#What does a nested conditional statement do? You can nest as many contidionals as you want but don't ever go past 3 because it gets confusing.
if num < 10:
    if num ==8:
        print("This prints at 8")
    else:
        if num == 4:
            print("There are only enough cookie left for me... sorry")
        else:
            print("The number is less than 10")
else: 
    print("The number is bigger than 10")

