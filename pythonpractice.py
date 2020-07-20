'''
File name: pythonpractice.py
Author: Hannah Lewis
Date created: 07/17/2020
Date last modified: 07/17/2020
Python Version: 3.7

These are a bunch of silly practice problems from practicepython.org. Exercises 1-10 are included here.
'''

def char_input():
    '''
    Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

    Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
    '''
    import time
    
    name = input("What is your name?: ")
    age = int(input("And (we know it's not polite to ask but...) what is your age (as a whole number, please)?: "))
    
    year, _, _, _, _ = map(int, time.strftime("%Y %m %d %H %M").split()) # Get the current year
    year_100 = year - age + 100 # Calculate what year they'll turn 100
    
    times = int(input("How many times would you like to see the message I'm about to print out?: "))
    
    for i in range(times):
        print("Hello, " + name + "! You will turn 100 years old in the year " + str(year_100) + ". Happy birthday!")
        
        i += 1
        
def odd_even():
    '''
    Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

    Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
    '''
    
    num = int(input("Give me an integer, please!: "))
    check = int(input("What number do you want to divide {} by?: ".format(num)))
    
    assert num > check, "We're only doing integer division here! The divisor you gave is larger than the dividend."
    
    if num % 4 == 0: # Mod
        print(str(num) + " is a multiple of 4.")
    elif num % 2 == 0:
        print(str(num) + " is an even number!")
    elif num % 2 == 1:
        print(str(num) + " is an odd number!")
    
    if num % check == 0:
        print("And it's also divisible by " + str(check) + ".")
    elif num % check == 1:
        print("It's not divisible by " +str(check) + " though.")
    
def list_less_than():
    '''
    Take a list, say for example this one:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list that are less than 5.

    Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
    '''
    
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # Sample list here, can be substituted/changed
    
    num = int(input("Give me an integer, please!: "))
    
    b = [x for x in a if x <= num] # List with numbers smaller than the input
    print(b)
    
def divisors():
    '''
    Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
    '''
    
    import numpy as np
    
    num = int(input("Give me an integer, please!: "))
    
    x = np.arange(1,num+1) # Generate an array of numbers between 1 and the number input
    
    div = []
    for n in x:
        if num % n == 0:
            div.append(n)
        else:
            continue
    
    print(str(num) + " is divisible by {}.".format(div))
    
def list_overlap():
    '''
    Take two lists, say for example these two:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
      b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

    Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
    '''
    
    import random
    
    n1 = random.randint(1,20) # Random length of first list
    a = random.sample(range(0, 50), n1) # First list of random length and random numbers

    n2 = random.randint(1,20) # Random length of second list
    b = random.sample(range(0, 50), n2) # Second list of random length and random numbers
    
    list_overlap = []
    for i in a:
        if i in b and i not in list_overlap: # Find intersection/overlap
            list_overlap.append(i)
    
    print(list_overlap)
    
def string_list():
    '''
    Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
    '''
    
    word = input("Input a word, and I'll check to see if it is a palindrome (not case sensitive): ")
    
    backwards = word[::-1] # Get the word, backwards

    if word.lower() == backwards.lower(): # Compares the strings, ignoring case
        print("The word is a palindrome!")
    else:
        print("The word is not a palindrome.")
    
def list_comp():
    '''
    Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
    '''
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [x for x in a if x % 2 == 0] # Get even elements
    
    print("Here is the original array: ", a)
    print("Here are the even elements from that array: ", b)
    
def rps():
    '''
    Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game).
    
    I'm actually going to make this a one-player vs. CPU game with random throws from the CPU

    Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
    '''
    
    import random
    
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
        
    while True:
    
        player = input("Rock, paper, scissors. Shoot! (enter your throw): ") # Get player throw
        
        n_rps = random.randint(0,2)
        rps_array = ['rock', 'scissors', 'paper']
        CPU_rps = rps_array[n_rps] # Get CPU throw
        
        assert player.lower() in rps_array, "Enter rock, paper, or scissors."
        assert CPU_rps.lower() in rps_array, "Enter rock, paper, or scissors."
        
        a = game_dict.get(player.lower())
        b = game_dict.get(CPU_rps.lower())
        
        dif = a - b
        
        print("CPU threw " + CPU_rps + ".")
    
        if dif in [-1,2]: # Compare throws to find winner
            print("Player wins!")
            if input("Do you want to play another game, yes or no?: ") == 'yes':
                continue
            else:
                print("Good game!")
                break
                
        elif dif in [-2,1]: # Compare throws to find winner
            print("CPU wins!")
            if input("Do you want to play another game, yes or no?: ") == 'yes':
                continue
            else:
                print("Good game!")
                break
                
        else: # Or tie
            print("It's a tie!")
            if input("Do you want to play another game, yes or no?: ") == 'yes':
                continue
            else:
                print("Good game!")
                break
                
def guessing_game():
    '''
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

    Extras:

    Keep the game going until the user types 'exit'
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
    '''
    
    import random
    
    print("You can type 'exit' at any time to end the game.")
    
    num = random.randint(1,9) # Get random number
    
    guess = input("Guess a number between 1 and 9: ") # Get first guess
    count = 0
    
    guessing = True
    
    while guessing:
        
        if guess == 'exit': # Player can exit at any time
            break
                        
        count += 1
            
        if num > int(guess):
            guess = input("Too low! Guess again: ")
        elif num < int(guess):
            guess = input("Too high! Guess again: ")
        elif num == int(guess):
            if count == 1:
                print("You got it on the first try!")
                guessing = False
            if count > 1:
                print("You got it! It took you", count, "tries.")
                guessing = False
        elif guess.lower() == 'exit':
            print("Better luck next time.")
            guessing = False
            
def list_overlap_v2():
    '''
    This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

    Take two lists, say for example these two:

        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python. (Hint: Remember list comprehensions from Exercise 7).

    Extra:

    Randomly generate two lists to test this
    '''
    
    import random
    
    n1 = random.randint(1,20) # Random length of first list
    a = set(random.sample(range(0, 50), n1)) # First set of random length and random numbers

    n2 = random.randint(1,20) # Random length of second list
    b = set(random.sample(range(0, 50), n2)) # Second set of random length and random numbers
    
    list_overlap = list(a & b) # Find intersection/overlap
    
    print(list_overlap)
    
    
function_dict = {'1':char_input, '2':odd_even, '3':list_less_than, '4':divisors, '5':list_overlap,
                 '6':string_list, '7':list_comp, '8':rps, '9':guessing_game, '10':list_overlap_v2} # What exercise corresponds to each function

exercise = input("Which exercise do you want to run?: ")
print("Exercise " + exercise)

function_dict[exercise]() # Runs exercise
    
