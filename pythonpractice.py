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
    Print out that many copies of the previous message on separate lines.
    '''
    import time
    
    print("This exercise will tell you in what year you will turn 100.\n")
    
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
    
    print("This exercise will tell you if a number is even or odd, and if it is divisible by another integer.\n")
    
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
    
    print("This exercise will tell you, from a predefined list of numbers, which ones are less than another number.\n")
    
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # Sample list here, can be substituted/changed
    
    num = int(input("Give me an integer, please!: "))
    
    b = [x for x in a if x <= num] # List with numbers smaller than the input
    print(b)
    
def divisors():
    '''
    Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
    '''
    
    import numpy as np
    
    print("This exercise will give you all the divisors of a number.\n")
    
    num = int(input("Give me an integer, please!: "))
    
    x = np.arange(1,num+1) # Generate an array of numbers between 1 and the number input
    
    div = []
    for n in x:
        if num % n == 0:
            div.append(n)
        else:
            continue
    
    print(str(num) + " is divisible by {}.".format(div))
    
    return(div)
    
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
    
    print("This exercise will generate two random lists of random lengths, and then tell you their intersection.\n")
    
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
    
    print("This exercise will tell you if a word is a palindrome.\n")
    
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
    
    print("This exercise will tell you all the even elements of a predefined list.\n")
    
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
    
    print("This exercise is an infinite game of Rock, Paper, Scissors between the player and the CPU.\n")
    
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
            if input("Do you want to play another game, yes or no?: ").lower() == 'yes':
                continue
            else:
                print("Good game!")
                break
                
        elif dif in [-2,1]: # Compare throws to find winner
            print("CPU wins!")
            if input("Do you want to play another game, yes or no?: ").lower() == 'yes':
                continue
            else:
                print("Good game!")
                break
                
        else: # Or tie
            print("It's a tie!")
            if input("Do you want to play another game, yes or no?: ").lower() == 'yes':
                continue
            else:
                print("Good game!")
                break
                
def guessing_game():
    '''
    Generate a random number between 1 and 10 (including 1 and 10). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

    Extras:

    Keep the game going until the user types 'exit'
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
    '''
    
    import random
    
    print("This exercise will ask you to guess what number the CPU has thought of.\n")
    
    print("You can type 'exit' at any time to end the game.")
    
    num = random.randint(1,10) # Get random number
    
    guess = input("Guess a number between 1 and 10: ") # Get first guess
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
    
    print("This exercise will generate two random lists of random lengths, and then tell you their intersection, using sets instead of list comprehension.\n")

    n1 = random.randint(1,20) # Random length of first list
    a = set(random.sample(range(0, 50), n1)) # First set of random length and random numbers

    n2 = random.randint(1,20) # Random length of second list
    b = set(random.sample(range(0, 50), n2)) # Second set of random length and random numbers
    
    list_overlap = list(a & b) # Find intersection/overlap
    
    print(list_overlap)
    
def check_prime():
    '''
    Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
    '''
    
    import numpy as np
    
    print("This exercise will tell you if a number is a prime number.\n")
        
    div = divisors() # Run divisors exercise
    
    if len(div) == 2:
        print("So it is a prime number!") # Prime if only divisible by 1 and itself
    else:
        print("It's NOT a prime number.")
        
def first_last():
    '''
    Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
    '''
    
    print("This exercise returns an array of the first and last elements of a predefined list.\n")
    
    a = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    
    print([a[0], a[-1]]) # Create list of first and last elements
    
    return [a[0], a[-1]]
    
def fib():
    '''
    Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
    '''
    
    print("This exercise returns list of Fibonacci numbers.\n")
    
    num = int(input("How many Fibonacci numbers would you like to generate?: "))
    
    i = 1
    
    if num == 0:
        f = []
    elif num == 1:
        f = [1]
    elif num == 2:
        f = [1, 1]
    else:
        f = [1, 1]
        while i < (num-1):
            f.append(f[i] + f[i-1])
            i += 1
    
    print(f)
    
    return f
    
def remove_duplicates():
    '''
    Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

    Extras:

    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.
    '''
    
    import random
    
    print("This exercise returns a unique list of numbers from a list.\n")
    
    n1 = random.randint(1,20) # Random length of list
    a = random.choices(range(1, 25), k=n1) # First list of random length and random numbers
    print(a)
    
    #b = []
    
    #for i in a:
        #if i not in b:
            #b.append(i)
                
    #return b
    
    print(list(set(a)))
    
    return list(set(a))
    
def reverse_word():
    '''
    Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

      My name is Michele
    Then I would see the string:

      Michele is name My
    shown back to me.
    '''
    
    print("This exercise returns words in the reverse order.\n")
    
    sentence = input("Write a sentence. ")
        
    print(' '.join(sentence.split(' ')[::-1]))
    
    return ' '.join(sentence.split(' ')[::-1])
    
def pass_gen():
    '''
    Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
    '''
    
    import string
    import random
    
    print("This exercise returns a randomly generated password.\n")
    
    length = int(input("How many characters do you want in your password? "))
    
    chars=string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))

    print("Here's your password: ", password)
    
    return password
    
def read_web_page():
    '''
    Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
    '''
    
    import requests
    from bs4 import BeautifulSoup
    
    print("This exercise returns a list of articles on the NYT homepage.\n")
    
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    site = 'https://www.nytimes.com/'
    response = requests.get(site,headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    for item in soup.select('.assetWrapper'):
        try:
            print('---------------------')
            headline = item.find('h2').get_text()
            link = item.find('a')['href']
            summary = item.find('p').get_text()
            print(headline)
            print(link)
            print(summary)
        except Exception as e: #raise e
            print('')
            
def cows_bulls():
    '''
    Create a program that will play the “cows and bulls” game with the user. The game works like this:

    Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
    '''
    
    import random
    
    print("This exercise is a game of Cow-Bull.\n")
    print("You will try to guess a random 4-digit number.\n")
    print("A 'cow' is a correct digit in the correct place.\n")
    print("A 'bull' is a correct digit in the wrong place.\n")
    print("The game ends when you get 4 cows!\n")
    
    print("You can type 'exit' at any time to end the game.")
    
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
        elif guess.lower() == 'exit': # If player wants to exit
            print("The number was " + str(num) + ".")
            print("Better luck next time.")
            guessing = False
        else: # Guess again
            cow = bull = 0
            guess = input("Guess again: ")
            
def read_web_page_v2():
    '''
    Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

    The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

    This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.
    '''
    
    import requests
    from bs4 import BeautifulSoup
    import csv
    
    print("This exercise returns the text of an article at a predefined URL to a text file called 'article.txt'.\n")
    
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    site = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    response = requests.get(site,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    article = soup.select('p')
    cleaned = []

    for i in article:
        temp = i.text.replace("<span>","")
        cleaned.append(temp)
    
    with open('article.txt','w') as txt:
        for line in cleaned:
            txt.write(line)
            
def elem_search():
    '''
    Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
    '''
    
    import random
    
    print("This exercise tells you if a number is in a random list of numbers.\n")
    
    num = int(input("Give me an integer, please! (between 1 and 100): "))

    n1 = random.randint(10,20) # Random length of list
    a = sorted(random.sample(range(1, 100), n1)) # List of random length and random numbers
    print(a)
    
    print(num in a)
    
    return num in a
    
def read_web_page_v3():
    '''
    Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

    Extras:

    Ask the user to specify the name of the output file that will be saved.
    '''

    import requests
    from bs4 import BeautifulSoup
    import csv

    print("This exercise returns the text of an article at a predefined URL to a text file named based on user input.\n")

    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    site = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    response = requests.get(site,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    article = soup.select('p')
    cleaned = []
    
    name = input("What do you want the file to be called?: ")

    for i in article:
        temp = i.text.replace("<span>","")
        cleaned.append(temp)

    with open(name + '.txt','w') as txt:
        for line in cleaned:
            txt.write(line)
            
def read_file():
    '''
    Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

    Extra:

    Instead of using the .txt file from above, take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3.
    '''
    
    print("This exercise opens a text file, reads the rows, and returns how many of each thing are in the file.\n")
    
    names_dict = {}
    with open('nameslist.txt','r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line in names_dict:
                names_dict[line] += 1
            else:
                names_dict[line] = 1
            line = f.readline()
            
    print(names_dict)
    
    scenes_dict = {}
    with open('SUNscenes.txt','r') as f:
        line = f.readline()
        while line:
            line = line[3:-26]
            if line in scenes_dict:
                scenes_dict[line] += 1
            else:
                scenes_dict[line] = 1
            line = f.readline()
            
    print(scenes_dict)
    
    return names_dict, scenes_dict

def file_overlap():
    '''
    Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

    (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.)
    '''
    
    print("This exercise opens two text files, reads the rows, and finds the overlap of the numbers in the files.\n")
    
    primes = []
    with open('primes.txt','r') as f:
        line = f.readline()
        while line:
            primes.append(int(line))
            line = f.readline()
    primes = set(primes)
    
    happy = []
    with open('happy.txt','r') as f:
        line = f.readline()
        while line:
            happy.append(int(line))
            line = f.readline()
    happy = set(happy)
    
    overlap = sorted(list(primes & happy))
    
    print(overlap)
            
    return overlap
    
def draw_gameboard():
    '''
    This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.

    Time for some fake graphics! Let’s say we want to draw game boards that look like this:

     --- --- ---
    |   |   |   |
     --- --- ---
    |   |   |   |
     --- --- ---
    |   |   |   |
     --- --- ---
     
    This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

    Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
    '''

    print("This exercise prints a square 2-D game board based on user input.\n")
    
    size = int(input("How large do you want your game board to be?: "))

    for x in range(size):
        print(' ---' * size)
        print('|   ' * (size+1))
    print(' ---' * size)
    
def guessing_game_v2():
    '''
    In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

    This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

    At the end of this exchange, your program should print out how many guesses it took to get your number.

    As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)
    '''

    import random
    import time

    print("This exercise will ask you to think of a number, and the CPU will try to guess the number.\n")

    print("You can type 'exit' at any time to end the game.")
    
    min = 1
    max = 100

    print("You have 5 seconds to think of a number between {} and {}...".format(min, max))
    
    time.sleep(5)
    
    count = 0
    CPU = random.randint(min,max) # Generate the first guess
    print("Okay, the CPU has the first guess: {}".format(CPU))
    
    answering = True

    while answering:
    
        ans = input("Is this the number you were thinking of? (yes, high, or low): ")
    
        if ans == 'exit': # Player can exit at any time
            break
                                
        count += 1
        
        if ans.lower() == 'yes':
            if count == 1:
                print("The CPU got it on the first try!")
                answering = False
            if count > 1:
                print("The CPU got it! It took", count, "tries.")
                answering = False
        elif ans.lower() == 'high':
            max = CPU-1
            CPU = random.randint(min,max) # Generate the next guess
            print("Guess: {}".format(CPU))
            answering = True
        elif ans.lower() == 'low':
            min = CPU+1
            CPU = random.randint(min,max) # Generate the next guess
            print("Guess: {}".format(CPU))
            answering = True
        elif ans.lower() == 'exit':
            print("Better luck next time, CPU!")
            answering = False
            
def check_tic_tac_toe():
    '''
    Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

    If a game of Tic Tac Toe is represented as a list of lists, like so:

    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]
    where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

    Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
    '''
    
    print("This exercise checks the winner of a game of tic-tac-toe.")
    
    def check_grid(grid):
    
        for x in range(0,3): # Define what a win looks like in a row
            row = set([grid[x][0],grid[x][1],grid[x][2]])
            if len(row) == 1 and grid[x][0] != 0:
                return grid[x][0]

        for x in range(0,3): # Define what a win looks like in a column
            column = set([grid[0][x],grid[1][x],grid[2][x]])
            if len(column) == 1 and grid[0][x] != 0:
                return grid[0][x]

        diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
        diag2 = set([grid[0][2],grid[1][1],grid[2][0]]) # Define what a win looks like on a diagonal
        if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
            return grid[1][1]
            
        return None
        
    winner_is_1 = [[1, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]
    winner_is_also_1 = [[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]
    winner_is_2 = [[2, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]
    no_winner = [[1, 2, 0],
                 [2, 1, 0],
                 [2, 1, 2]]
    also_no_winner = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 0]]
    first_move = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]
                      
    assert check_grid(winner_is_1) == 1, "Got the wrong winner"
    assert check_grid(winner_is_also_1) == 1, "Got the wrong winner"
    assert check_grid(winner_is_2) == 2, "Got the wrong winner"
    assert check_grid(no_winner) == None, "Got the wrong winner"
    assert check_grid(also_no_winner) == None, "Got the wrong winner"
                   
    print(check_grid(first_move))
    
def tic_tac_toe():
    '''
    The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

    As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:

    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out

    game = [[0, 0, X],
            [0, 0, 0],
            [0, 0, 0]]
    And ask Player 2 for their move, printing an O in that place.

    Things to note:

    For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
    Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this, it should be explained to the player.
    Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. Then you can use your Python skills to figure out which row and column they want their piece to be in.
    Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
    Bonus:

    For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.
    '''
    
    print("This exercise is a game of tic-tac-toe!")
    
    print("You can type 'exit' at any time to end the game.")
    
    def check_grid(grid):

        for x in range(0,3): # Define what a win looks like in a row
            row = set([grid[x][0],grid[x][1],grid[x][2]])
            if len(row) == 1 and grid[x][0] != 0:
                return grid[x][0]

        for x in range(0,3): # Define what a win looks like in a column
            column = set([grid[0][x],grid[1][x],grid[2][x]])
            if len(column) == 1 and grid[0][x] != 0:
                return grid[0][x]

        diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
        diag2 = set([grid[0][2],grid[1][1],grid[2][0]]) # Define what a win looks like on a diagonal
        if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
            return grid[1][1]
    
        return 0
        
    def check_winner(grid):
        winner = check_grid(grid)
        return winner
    
    turn = 0
    winner = 0
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
            
    playing = True

    while playing and winner == 0:
    
        if turn % 2 == 0:
            player_turn = '1'
        else:
            player_turn = '2'
        
        if turn % 2 == 0:
            player_s = 'X'
        else:
            player_s = 'O'
        play = input("Player {}, your turn! Where would you like to place your {} (row, col): ".format(player_turn, player_s))
        
        if play == 'exit': # Player can exit at any time
            break
    
        col, row = play.split(',')
        col = int(col)
        row.strip(' ')
        row = int(row)
        
        if game[col-1][row-1] != 0:
            print('\nMust select an empty space which is not occupied by a player')
            continue
        else:
            game[col-1][row-1] = str(player_s)
    
        print(game[0], '\n', game[1], '\n', game[2])
        
        winner = check_winner(game)
    
        turn += 1
        
    if winner != 0:
        print("Player {} wins!".format(player_turn))
        
def max_of_three():
    '''
    Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

    The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!
    '''
    
    print("This exercise finds the largest of three numbers in a list, without using the max() function.")
    
    list = input("Give a list of 3 numbers, separated by commas: ")
    
    n1, n2, n3 = list.split(',')
    n1 = float(n1.strip(' '))
    n2 = float(n2.strip(' '))
    n3 = float(n3.strip(' '))
    
    max = n1
    
    if n2 > max:
        max = n2
    if n3 > max:
        max = n3

    print(str(max) + " is the largest number in the list you gave.")
    
    return max


if __name__ == '__main__':

    function_dict = {'1':char_input, '2':odd_even, '3':list_less_than, '4':divisors, '5':list_overlap,
                     '6':string_list, '7':list_comp, '8':rps, '9':guessing_game, '10':list_overlap_v2,
                     '11':check_prime, '12':first_last, '13':fib, '14':remove_duplicates, '15': reverse_word,
                     '16':pass_gen, '17':read_web_page, '18':cows_bulls, '19':read_web_page_v2, '20':elem_search,
                     '21':read_web_page_v3, '22':read_file, '23':file_overlap, '24':draw_gameboard, '25':guessing_game_v2,
                     '26':check_tic_tac_toe, '27':tic_tac_toe, '28':max_of_three} # What exercise corresponds to each function

    exercise = input("Which exercise do you want to run?: ")
    print("Exercise " + exercise)

    function_dict[exercise]() # Runs exercise
    
