'''
File name: pythonpractice.py
Author: Hannah Lewis
Date created: 08/03/2020
Date last modified: 08/03/2020
Python Version: 3.7
'''

import random
    
def pick_word():
    '''
    This exercise is Part 1 of 3 of the Hangman exercise series.
    
    In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
    '''
            
    words = []
    with open('sowpods.txt','r') as f: # Open the SOWPODS dictionary txt files
        line = f.readline() # Read line
        while line:
            words.append(line) # Add to the list of words
            line = f.readline() # Read line
            
    random_word = random.choice(words) # Choose a random word
    
    #print("Here's your random word: ", random_word)
    
    return random_word
    
def letters():
    '''
    This exercise is Part 2 of 3 of the Hangman exercise series.

    In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).
    '''
    
    def print_hangman(wrong): # Graphics
        gallows = [[' ----  '],
                   ['|    | '],
                   ['|      '],
                   ['|      '],
                   ['|      '],
                   ['|      ']]
                   
        if wrong > 0:
            gallows[2] = ['|    O ']
        if wrong > 1:
            gallows[3] = ['|    | ']
        if wrong > 2:
            gallows[3] = ['|   /| ']
        if wrong > 3:
            gallows[3] = ['|   /|\\']
        if wrong > 4:
            gallows[4] = ['|   /  ']
        if wrong > 5:
            gallows[4] = ['|   / \\']
            
        for i in gallows:
            print(''.join(i))
            
        return
    
    random_word = list(pick_word().strip('\n')) # Remove new line and make word into a list
    
    guessed = list('_'*len(random_word)) # Make blanks
    
    guessed_list = [] # List of guessed letters
        
    wrong = 0 # Count the number of wrong guesses to determine when the hangman is complete and the game is lost
    
    playing = True
    
    print(' '.join(guessed)) # Print out the blanks

    while playing:
    
        letter = input("Guess a letter: ") # Get player guess
        
        if letter == 'exit': # Player can exit at any time
            print("Play again soon!")
            playing = False
            break
            
        if letter.upper() in guessed: # Don't allow a letter to be guessed twice
            letter = ''
            print("You already guessed that letter!")
            continue
            
        elif letter.upper() in random_word: # Letter in word, fill in blank, and add to guessed letters list
            for idx, l in enumerate(random_word): # Iterate through all the letters in the word in case the letter is used multiple times
                if letter.upper() == l: # Get indices
                    guessed[idx] = letter.upper() # Fill in blank corresponding to index
                    guessed_list.append(letter.upper()) # Add letter to guessed letters list
            print(' '.join(guessed)) # Print out the blanks and letters
            print_hangman(wrong) # Show graphics
            print("\n\n")
            
        else: # Letter not in word, add to guessed letters list and add to wrong guess count
            if letter.isalpha():
                guessed_list.append(letter.upper()) # Add letter to guessed letters list
                print("{} is not in the word!\n".format(letter.upper()))
                print(' '.join(guessed)) # Print out the blanks and letters
                wrong += 1 # Add to wrong guess count
                print_hangman(wrong) # Show graphics
                print("\n\n")
            else:
                print("Input must be a single letter, not a number or symbol.\n")
                continue
        
        if wrong == 6: # The hangman is complete
            print("Uh oh! You ran out of tries. The word was {}.".format(''.join(random_word)))
            playing = False
            break
                                
        if '_' not in guessed:
            print("You got it!")
            playing = False
            break
        
    #TODO: ask if they want to play another game
        
def main():
    '''
    This exercise is Part 3 of 3 of the Hangman exercise series.

    In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses. Copy your code from Parts 1 and 2 into a new file as a starting point.
    '''
    
    print("Ready to play a game of hangman?\n")
    
    print("You can type 'exit' at any time to end the game.\n")
    
    letters()


if __name__ == '__main__':

    main() # Runs exercise
    
