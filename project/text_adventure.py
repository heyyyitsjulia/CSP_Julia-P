#Text based adventure game, python
print("Hello player, welcome to our text based adventure game! Pick 1 of the each of the 2 puzzles to solve.")
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
            print("You are correct! Wow, you're good at this! You got jean overalls with embroidered flowers on the pockets.")  
            break  
        else:  
            print("That is WRONG, try again:")  
else:  
    print("That is not a valid option. Please pick 7 or 8.")  






puzzleone = int(input("pick a number, 1 or 2\n"))
if puzzleone == 1:
    while True:  
question = input("guess the qord based on the description! red, summer,fruit, sliced:\n")  
if question == "watermelon":
print("you are correct!\n You get granny white hair!")
break
    else:
print("that is incorrect, try again:")
 elif questiontwo == 2:  
 while Tfinishtiontwo = input("Finish the sequence! 156723451567234515672:\n")if finish == "345":
print("you are correct! You get light up neon circus afro hair!")
     
  
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



sequence = int(input("Pick either number 5 or 6 for your next puzzle.\n"))
if sequence == 5:
  while True:
    sequence_puzzle = input("What is the next number in the sequence? one, three, four, five, nine, two, eleven, four,...")
    if sequence_puzzle =="fifteen":
     print(f"That's correct! {sequence_puzzle} is the answer. You are wearing purple heelys. ")
     break
    else:
      print("That is incorrect, try again.")
elif sequence == 6:
  while True:
    sequence_puzzle_two = input("What is the next letter in the sequence? a, d, h, k, o, r,...")
    if sequence_puzzle_two =="u":
     print(f"That's correct! {sequence_puzzle_two} is the answer. You are wearing pink bedazzeled justice glow up sneakers! ")
     break
    else:
      print("That is incorrect, try again.")
        



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
            print("You are correct! Wow, you're good at this! You got jean overalls with embroidered flowers on the pockets.")  
            break  
        else:  
            print("That is WRONG, try again:")  
else:  
    print("That is not a valid option. Please pick 7 or 8.")  
