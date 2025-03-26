#Text based adventure game, python
print("Hello player, welcome to our text based adventure game! Pick 1 of the each of the 2 puzzles to solve.")
 
question = input ("choose a number! 1 or 2!\n")
if question == 1:
    print("finish the sequence!\n")
    print("156723451567234515672\n")
if  question == ("156723451567234515672\n"):
    input == ("345") 
    print("you are correct!\n You get granny white hair.")
else:
    print ("Find the word based on the description!")
    question == (" Red, summer, fruit, sliced.\n")

    input == ("watermelon")
hai = print(input("you have white granny hair!"))
hair = print(input("you have lilac hair!"))

secondquestion = input ("pick a number, 7 or 8")
while True:  
    riddle_answer = input("Here is your riddle, What is always on the floor, but never gets dirty:\n")  
    if riddle_answer == "shadow":  
        print("You are correct!\n You got a big blue ball gown with elegant puffed sleeves.")  
        break   
    else:  
        print("That is incorrect, try again:")  

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

