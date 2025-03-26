#riddle_answer = input ("Here is your riddle, What is always on the floor, but never gets dirty:\n")
#if riddle_answer == "shadow":
    #print(f"You are correct! {riddle_answer}was the answer.")
#else:
    #input(f"That is incorrect, try again!\n")
#while riddle_answer == "shadow":
secondquestion = input ("pick a number, 7 or 8")
while True:  
    if 7 == secondquestion:
        riddle_answer = input("Here is your riddle, What is always on the floor, but never gets dirty:\n")  
    if riddle_answer == "shadow":  
        print("You are correct!\n You got a big blue ball gown with elegant puffed sleeves.")  
        break 
    else:  
        print("That is incorrect, try again:")  
    if 8 == secondquestion: 
        unscramble = input("Unscramble this word... ")
