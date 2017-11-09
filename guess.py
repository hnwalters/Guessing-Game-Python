#Hayden N. Walters
""" In Python you need less characters to get the same end result. User input does not need its own line of code in Python, as it does in Java In Python there is no need to state whether the class is public or private, it is assumed public.  """
from random import randint
import random
def generateRandom(): # Generates a random number.
    z = int(input('Input a number to set as the high end of the range.\n'))
    random_num = randint(1,z)
    return random_num

def game(RandNumb): # the game function, runs the game
    triumph = False
    while not triumph:
        #print (RandNumb)# Prints the randomly generated number for debugging purposes.
        guess = int(input('Please enter a guess. \n'))
        if guess < RandNumb: # checks if user input is less than random number
            print ('Too low')
            insultgen()
        elif guess > RandNumb: #checks if user input is greater than random number
            print ('Too high')
            insultgen()
        else: # if it is neither lesser than or greater than the random number the user input is equal to the random number
            print ('Good job, you got it!')
            triumph = True

def insultgen(): # prints one of the insults listed randomly after each failed guess
    ins = ['Come on you are better than this.', 'You can not be this dumb.', 'Are you kidding me, right now?', 'My heavens you really are a dolt.','Your incompetence is insulting.']
    print(random.choice(ins))
    
cont = True #askes user if they wish to continue
while cont:
    game(generateRandom())
    answered = False
    while not answered:
        x = input ('Want to play again, type Y for yes and N for no (case does not matter).\n')
        if x.lower() == 'y': # continues the game
            cont = True
            answered = True
        elif x.lower() == "n": # ends the game
            print ('Thank you, come again.')
            cont = False
            answered = True
        else:
            print ('Not a valid input.') # asks question again
