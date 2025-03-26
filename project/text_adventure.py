#Text based adventure game, python
print("Hello player, welcome to our text based adventure game! Pick 1 of the each of the 2 puzzles to solve.")
while True:  
    question = input("choose a number! 1 or 2!\n")  
    if question == "1":  
        # your code for question "1"  
    elif question == "2":  
        # your code for question "2"  
while True:
question = input ("choose a number! 1 or 2!\n")
    if question is = 1 or sequence = 2
        if 1 == question:
        question = input("Finish the sequence! 156723451567234515672\n")
    if question == "345":
    print(f"that is correct! {question} is correct! You get granny white hair!" )
        break 
    else:
    print("That is incorrect! try again!")

if 2 == question:
    question_two = input("Find the worde based on the description! Red, summer, friut, sliced.")
if  question_two == ("watermelon"):
    print(f"{question_two} is correct! You get light up neon circus afro hair!")
    break
else:
    print("you are wrong! try again!")


while True:    
    puzzle = input("To pick 1 a word scramble or riddle, insert 3 or 4.\n")    
    if puzzle == "3":   
        answer = input("imekilcr\n")   
        if answer.lower() == "limerick":
            print("Correct, you won black eyes!\n") 
            break  
        else:
            print("Incorrect, try again...\n")
    elif puzzle == "4":  
        answer = input("Maria has five children. Jack, Logan, Sarah, and Lipton. What is the name of the fifth child?\n")    
        if answer.lower() == "what":    
            print("Correct, you won green eyes!\n")    
            break   
        else:    
            print("Incorrect, try again...\n")    
    else:  
        print("To pick 1 a word scramble or riddle, insert 3 or 4.\n")  



secondquestion = int(input("pick a number, 7 or 8\n"))    
  
if secondquestion == 7:    
    while True:    
        riddle_answer = input("Here is your riddle, What is always on the floor, but never gets dirty:\n")    
        if riddle_answer == "shadow":    
            print("You are correct!\n You got a big blue ball gown with elegant puffed sleeves.")    
            break   
        else:    
            print("That is incorrect, try again:")  
elif secondquestion == 8:   
    while True:  
        unscramble = input("Unscramble this word... stcilvaiiznoi:\n")  
        if unscramble == "civilizations":  
            print("You are correct! Wow, you're good at this! You got overalls with embroidered flowers on the pockets.")  
            break  
        else:  
            print("That is WRONG, try again:")  
else:  
    print("That is not a valid option. Please pick 7 or 8.")  
