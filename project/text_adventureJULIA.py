#riddle_answer = input ("Here is your riddle, What is always on the floor, but never gets dirty:\n")
#if riddle_answer == "shadow":
    #print(f"You are correct! {riddle_answer}was the answer.")
#else:
    #input(f"That is incorrect, try again!\n")
#while riddle_answer == "shadow":

while True:  
    riddle_answer = input("Here is your riddle, What is always on the floor, but never gets dirty:\n")  
    if riddle_answer == "shadow":  
        print("You are correct!\n You got a big blue ball gown with elegant puffed sleeves.")  
        break  # This exits the loop  
    else:  
        print("That is incorrect, try again:")  
