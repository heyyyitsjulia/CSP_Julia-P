#riddle_answer = input ("Here is your riddle, What is always on the floor, but never gets dirty:\n")
#if riddle_answer == "shadow":
    #print(f"You are correct! {riddle_answer}was the answer.")
#else:
    #input(f"That is incorrect, try again!\n")
#while riddle_answer == "shadow":

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

