# text adventure, python, elizabeth

print("Hello player, welcome to our text-based adventure game! Pick 1 of the 2 puzzles to solve.")  
  
player_traits = []  # List to store the traits the player wins  
  
# First puzzle selection  
puzzleone = int(input("Pick a number, 1 or 2\n"))  
if puzzleone == 1:  
    while True:    
        question = input("Guess the word based on the description! Red, summer, fruit, sliced:\n")    
        if question.lower() == "watermelon":  
            print("You are correct!\nYou get granny white hair!")  
            player_traits.append("granny white hair")  # Add the trait  
            break  
        else:  
            print("That is incorrect, try again:")  
  
elif puzzleone == 2:    
    while True:  
        finish = input("Finish the sequence! 156723451567234515672:\n")  
        if finish == "345":  
            print("You are correct! You get neon rainbow afro hair!")  
            player_traits.append("neon rainbow afro hair")  # Add the trait  
            break  
        else:  
            print("Loser! You're wrong! Do it again!")  
else:  
    print("That is not an option, pick 1 or 2.")  
  
# This section made by Elizabeth Gutierrez.
puzzle = int(input("Insert 3 or 4.\n"))     
if puzzle == 3:  
    while True:         
        answer = input("Unscramble this word: imekilcr\n")     
        if answer.lower() == "limerick":  
            print("Correct, you won black eyes!\n")   
            player_traits.append("black eyes")  # Add the trait  
            break    
        else:  
            print("Incorrect, try again...\n")  
elif puzzle == 4:   
    while True:   
        answer = input("Maria has five children. Jack, Logan, Sarah, and Lipton. What is the name of the fifth child?\n")  
        if answer.lower() == "what":      
            print("Correct, you won green eyes!\n")      
            player_traits.append("green eyes")  # Add the trait  
            break     
        else:      
            print("Incorrect, try again...\n")  
else:    
    print("That is not an option, insert 3 or 4.\n")    

  
sequence = int(input("Pick either number 5 or 6 for your next puzzle.\n"))  
if sequence == 5:  
    while True:  
        sequence_puzzle = input("What is the next number in the sequence? one, three, four, five, nine, two, eleven, four,... ")  
        if sequence_puzzle.lower() == "fifteen":  
            print("That's correct! You are wearing purple heelys.")  
            player_traits.append("purple heelys")  # Add the trait  
            break  
        else:  
            print("That is incorrect, try again.")  
elif sequence == 6:  
    while True:  
        sequence_puzzle_two = input("What is the next letter in the sequence? a, d, h, k, o, r,... ")  
        if sequence_puzzle_two.lower() == "u":  
            print("That's correct! You are wearing pink bedazzled justice glow up sneakers!")  
            player_traits.append("pink bedazzled justice glow up sneakers")  # Add the trait  
            break  
        else:  
            print("That is incorrect, try again.")  
  
# Puzzles 7 and 8  
secondquestion = int(input("Pick a number, 7 or 8\n"))      
if secondquestion == 7:      
    while True:  
        riddle_answer = input("Here is your riddle: What is always on the floor, but never gets dirty?\n")      
        if riddle_answer.lower() == "shadow":      
            print("You are correct!\nYou got a big blue ball gown with elegant puffed sleeves.")      
            player_traits.append("big blue ball gown with elegant puffed sleeves")  # Add the trait  
            break     
        else:  
            print("That is incorrect, try again:")    
elif secondquestion == 8:     
    while True:  
        unscramble = input("Unscramble this word: stcilvaiiznoi:\n")    
        if unscramble.lower() == "civilizations":    
            print("You are correct! Wow, you're good at this! You got jean overalls with embroidered flowers on the pockets.")    
            player_traits.append("jean overalls with embroidered flowers on the pockets")  # Add the trait  
            break    
        else:    
            print("That is WRONG, try again:")    
else:    
    print("That is not a valid option. Please pick 7 or 8.")    

print("Your character has:", ", ".join(player_traits))  
