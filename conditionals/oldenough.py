# Julia Properzi, Old enough python

num = int(input("How old are you:\n"))

if num >= 18:
    print("You can vote!")
elif num >= 16:
    print("You can drive!")
elif num >= 15:
    print("You can get your learners permit!")
elif num > 4:
    print("You can go to school!")
else:
    print("You cant go to school...")