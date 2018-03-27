import random

response1 = "It's nice to see you!"
response2 = "How was your day?"
response3 = "Nice weather, isn't it?"

#myName is a string that holds the user's name
myName = input("What's your name? ")

randomNumber = random.randint(1, 3)

if randomNumber == 1:
    print("Hi " + myName + "! " + response1)
elif randomNumber == 2:
    print("Hi " + myName + "! " + response2)
else:
    print("Hi " + myName + "! " + response3)


hearJoke = input("Would you like to hear a knock-knock joke? (Y or N) ")
while hearJoke != "Y" and hearJoke != "N":
    hearJoke = input("Please enter Y or N! ")

if hearJoke == "N":
    print("Okay! Have a nice day!")
    
elif hearJoke == "Y":
    anyInput = input("Knock knock! ") #We won't do anything with this
    # "Who's there?"
    
    randomNumber = random.randint(3, 7)
    for number in range(randomNumber):
        anyInput = input("Banana! ")
        # "Banana who?"
    print("Orange you glad I didn't say banana?")
        
