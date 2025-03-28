#Text based adventure game, python

print("Hello player, welcome to our text-based adventure game! As you solve the puzzles you will get different traits for your character. Pick 1 of the 2 puzzles to solve.") #Welcomes player to game, lets them choose which puzzle to solve. 
  
player_traits = []  #A list to store the traits the player wins  
  
# these two were made by Sariah Kamore.
puzzleone = int(input("Pick a number, 1 or 2\n"))  #this tells them the 2 options they can choose from
if puzzleone == 1:  #if they choose puzzle one it will give them a discription of a word they must solve
    while True:    #this is a while true statment that runs the code again if the answer it wrong(it helps loop the code)
        question = input("Guess the word based on the description! Red, summer, fruit, sliced:\n")    
        if question.lower() == "watermelon":  #this is the answer to puzzle 1
            print("You are correct!\nYou get granny white hair!")  #this is the trait that they get if they solve it correctly
            player_traits.append("granny white hair")  # Add the trait  
            break  
        else:  
            print("That is incorrect, try again:")  #this tells them that the answer they put is wrong and that they need to do the puzzle again
  
elif puzzleone == 2:    #if they pick puzzle 2 then they need to solve the puzzle that is in puzzle 2
    while True:  
        finish = input("Finish the sequence! 156723451567234515672:\n")  #the puzzle for puzzle 2 that they need to solve
        if finish == "345":  #the answer they need to solve for and put in correctly
            print("You are correct! You get neon rainbow afro hair!")  #the attribute in their looks they get
            player_traits.append("neon rainbow afro hair")  # Add the trait  
            break  
        else:  
            print("Loser! You're wrong! Do it again!")  #this tells the player that they are incorrect and need to do the puzzle correctly/ enter the correct answer
else:  
    print("That is not an option, pick 1 or 2.")  #this makes it so that the player cannot pick another number apart from 1 or 2
  
# This section made by Elizabeth Gutierrez. 
puzzle = int(input("Insert 3 or 4.\n"))     #Allows user to choose whether they want puzzle 3 or 4.
if puzzle == 3:  
    while True:      #if they pick three, they get the question for puzzle 3. 
        answer = input("Unscramble this word: imekilcr\n")     
        if answer.lower() == "limerick":  #The answer they need to get.
            print("Correct, you won black eyes!\n")  #they win black for for correctly answering Q3 
            player_traits.append("black eyes")  # Adds the trait  
            break    #Exists the loop.
        else:  
            print("Incorrect, try again...\n")  #Makes the having to keep answering if they don't put the correct answer.
elif puzzle == 4:   
    while True:   #if they pick 4, they get the puzzle option for 4.
        answer = input("Maria has five children. Jack, Logan, Sarah, and Lipton. What is the name of the fifth child?\n")  
        if answer.lower() == "what":      
            print("Correct, you won green eyes!\n")  #Win green eyes if they correctly answer Q4  
            player_traits.append("green eyes")  # Adds the trait  
            break     
        else:      
            print("Incorrect, try again...\n") #Makes the having to keep answering if they don't put the correct answer.
else:    
    print("That is not an option, insert 3 or 4.\n")   # makes user insert 3 or 4 and nothing else, in order to do their puzzle.

#These two were written by Paige Jolley
sequence = int(input("Pick either number 5 or 6 for your next puzzle.\n"))  
if sequence == 5: #If the user picked this one then the code would print but if they picked the other number it would print the other puzzle. 
    while True:  #This is a while statement, while it stays true, then the code stays a certain way.
        sequence_puzzle = input("What is the next number in the sequence? one, three, four, five, nine, two, eleven, four,... ")  
        if sequence_puzzle.lower() == "fifteen":  
            print("That's correct! You are wearing purple heelys.")  
            player_traits.append("purple heelys")  # This adds the trait to list
            break  
        else:  
            print("That is incorrect, try again.")  #Here the code loops back to the beginning, so they get a chance to retry the puzzle.
elif sequence == 6:  
    while True:  
        sequence_puzzle_two = input("What is the next letter in the sequence? a, d, h, k, o, r,... ")  
        if sequence_puzzle_two.lower() == "u":  
            print("That's correct! You are wearing pink bedazzled justice glow up sneakers!")  
            player_traits.append("pink bedazzled justice glow up sneakers")  # This the trait  to list
            break  
        else:  
            print("That is incorrect, try again.")  
  
# This part is written by Julia Properzi  
secondquestion = int(input("Pick a number, 7 or 8\n"))   
#These are if else statements, that depending on if the statements are true then the code will continue onto the rest of the code.   
if secondquestion == 7:      
    while True:  #Here is a while true statement that runs until you get the question incorrect, when it breaks, causing there to be a different printed output.
        riddle_answer = input("Here is your riddle: What is always on the floor, but never gets dirty?\n")      
        if riddle_answer.lower() == "shadow":      
            print("You are correct!\nYou got a big blue ball gown with elegant puffed sleeves.")      
            player_traits.append("big blue ball gown with elegant puffed sleeves")  # Adds the trait  
            break     
        else:  
            print("That is incorrect, try again:")    
elif secondquestion == 8:     
    while True:  
        unscramble = input("Unscramble this word: stcilvaiiznoi:\n")    
        if unscramble.lower() == "civilizations":    
            print("You are correct! Wow, you're good at this! You got jean overalls with embroidered flowers on the pockets.")    
            player_traits.append("jean overalls with embroidered flowers on the pockets")  # Adds the trait  
            break    
        else:    
            print("That is WRONG, try again:")    
else:    
    print("That is not a valid option. Please pick 7 or 8.")    

print("Your character has:", ", ".join(player_traits))  #This part puts in the traits that the user won throughout the game, and puts it all in one description.