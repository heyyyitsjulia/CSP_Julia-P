# Julia Properzi, Functions Notes python

#funcions hold actions to be reused

#def add():
   # numOne = int(input("Please tell me a number:\n"))
   # numTwo = int(input("Tell me another number: \n"))

#number = int(input("Please tell me a number:\n"))
#def add(numOne, numTwo): #parameter set the name of the variable(just for the funcion)
 #   return numOne + numTwo
    #print (numOne+numTwo)

#print (add(number,21)) #arguments set the value of the variable just for that instance of the function
#print(add(8,12))
#addition = add(6,4)
#print(add(11,10000))
#add(3,67)

def values(type):
    return input(f"Please give me a {type}:\n")
name =values("name")
place =values("place")
verb = values("verb")

print(f"{name} was really fast getting to {place} because they were {verb} the whole way there.")