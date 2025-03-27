#Julia Properzi, Variable

subject = input("What's your favorite subject: ")

small_number = 4

name = input("what is your name: ")

print(name, "really likes", subject)

name = "Alex"

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