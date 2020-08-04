'''
File name: pythonpractice.py
Author: Hannah Lewis
Date created: 08/03/2020
Date last modified: 08/03/2020
Python Version: 3.7
'''

import random
    
def main():
    '''
    Create a program that will play the “cows and bulls” game with the user.
    '''
        
    print("You will try to guess a random 4-digit number.")
    print("A 'cow' is a correct digit in the correct place.")
    print("A 'bull' is a correct digit in the wrong place.")
    print("The game ends when you get 4 cows!\n")
    
    print("You can type 'exit' at any time to end the game.\n")
    
    num = str(random.randint(10000, 99999))[1:5] # Get random number, remove first digit so that first digit can be 0
    
    guess = input("Give me your best guess: ") # Get first guess
    
    count = 0
    cow = 0
    bull = 0
    
    guessing = True
    
    while guessing:
    
        assert len(guess) == 4, "Input must be 4-digits long."
    
        if guess == 'exit': # Player can exit at any time
            print("The number was " + str(num) + ".")
            print("Better luck next time.")
            guessing = False
            break
                
        count += 1
        
        for i in range(0,4): # Compare digits
            if num[i] == guess[i]:
                cow+=1
            elif num[i] in guess:
                bull+=1
        print("You got {} cows, and {} bulls.".format(cow,bull)) # How many cows and bulls
        
        if cow == 4: # If all digits are correct
            if count == 1:
                print("You got it on the first try!")
                guessing = False
            if count > 1:
                print("You got it! It took you", count, "tries.")
                print("The number was " + str(num) + ".")
                guessing = False
        else: # Guess again
            cow = bull = 0
            guess = input("Guess again: ")
            
    #TODO: ask if they want to play another game
            
    return

if __name__ == '__main__':

    print("Ready to Cows and Bulls?")

    main() # Runs exercise
    
