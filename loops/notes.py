# Julia Properzi,, Loops notes python

#What is a loop? 
    #a section of code that repeats multiple times
#What are the two types of loops?
    #for loop
nums = [12,3,66,7,3,3,2]

for num in nums: 
    print(num)

    #While loop
    x = 0

while x < 10:
    print(x)
    x+=1
#What is iteration?
    #one particular instance of the loop
    #iteration the amount of times you are looping through

#What are lists? 
    #a variable that holds multiple values
nums = [1,2,3,4,5,6,7,6]
siblings = ["Alex","Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Hailey"]
print(nums) #prints whole list is ugly
print(siblings[3]) #prints 1 item from the list

siblings[7] = "Jake" #can replace the name in the list
siblings.pop(5) #removes something from the list
siblings.insert(1,"Jayshree") #Can add to the list
siblings.insert(2, ["Joe", "Noah", "Zee"]) #can put list in list
print(siblings) 

#How do you make lists in python? 
#To make a list, step one is brackets
#step two you add in items with correct data types
#Step three, you need to have a comma between each item

#How do you make for loops in python? (use plural)
for sibling in siblings:
    print(sibling)

for x in range(1,101, 20):
    print(x)
#How do you make while loops in python?
import random 
x = 1 #variable to keep count of iteration
goose = random.randint(1,20)

while x < 20:
    if x == goose:
        print("goose!")
        break #tells loop to stop
    #continue sends back to while and starts infinate loop
    else:
        print("duck")
    x+=1

    #continue moves on to the next iteration without finishing