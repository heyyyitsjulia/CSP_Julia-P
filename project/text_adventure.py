#Text based adventure game, python
print("Hello player, welcome to our text based adventure game! Pick 1 of the each of the 2 puzzles to solve.")
puzzleone = int(input("pick a number, 1 or 2\n"))
if puzzleone == 1:
    while True:  
        question = input("guess the word based on the description! red, summer,fruit, sliced:\n")  
        if question == "watermelon":
            print("you are correct!\n You get granny white hair!")
            break
        else:
            print("that is incorrect, try again:")

elif puzzleone== 2:  
    while True:
        finish = input ("Finish the sequence! 156723451567234515672:\n")
        if finish == "345":
            print("you are correct! You get neon ranbow afro hair!")
            break
        else:
            print("Loser! You're wrong! Do it again!")
else:
    print("That is not an option, pick 1 or 2..")
        

        

puzzle = int(input("Insert 3 or 4.\n"))   
if puzzle == 3:
    while True:       
        answer = input("unscramble this word scramble. imekilcr\n")   
        if answer == "limerick":
            print("Correct, you won black eyes!\n") 
            break  
        else:
            print("Incorrect, try again...\n")
elif puzzle == 4: 
    while True: 
        answer = input("Maria has five children. Jack, Logan, Sarah, and Lipton. What is the name of the fifth child?\n")
        if answer == "what":    
            print("Correct, you won green eyes!\n")    
            break   
        else:    
            print("Incorrect, try again...\n")    
    else:  
        print("That is not an opton, insert 3 or 4.\n")  

#These two were written by Paige Jolley
sequence = int(input("Pick either number 5 or 6 for your next puzzle.\n"))# This making them be able
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




#These are statements 
puzzles = ["Black eyes", "granny white hair", "big blue ball gown with elegant puffed sleeves", "purple heelys"]
for puzzle in puzzles:
    print("Your character has", puzzle)

prizes = ["Green eyes", "light up neon circus afro hair", "jean overalls with embroidered flowers on the pockets", "pink bedazzeled justice glow up sneakers"]
for prize in prizes:
    print("Your character has", prize)

wins = ["Black", "light up neon circus afro hair", "big blue ball gown with elegant puffed sleeves", "pink bedazzled justics glow up sneakers"]
for win in wins:
    print("Your character has", win)

selects = ["Green eyes", "granny white hair", "jean overalls with embroidered flowers on the pockets", "purple heelys"]
for select in selects:
    print("Your character has", select)