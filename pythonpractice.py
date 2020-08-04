'''
File name: pythonpractice.py
Author: Hannah Lewis
Date created: 07/17/2020
Date last modified: 08/03/2020
Python Version: 3.7

These are a bunch of silly practice problems from practicepython.org.
'''

def char_input():
    '''
    Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

    Extras:
    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
    Print out that many copies of the message on separate lines.
    '''
    import time
    
    print("This exercise tells you in what year you will turn 100.\n")
    
    name = input("What is your name?: ") # Get name
    age = int(input("And (we know it's not polite to ask but...) what is your age (as a whole number, please)?: ")) # Get age
    
    year, _, _, _, _ = map(int, time.strftime("%Y %m %d %H %M").split()) # Get current year
    year_100 = year - age + 100 # Calculate what year they'll turn 100
    
    times = int(input("How many times would you like to see the message I'm about to print out?: "))
    
    for i in range(times):
        print("Hello, " + name + "! You will turn 100 years old in the year " + str(year_100) + ". Happy birthday!")
        i += 1 # Print message again
        
    return year_100
        
def odd_even():
    '''
    Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

    Extras:
    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
    '''
    
    print("This exercise will tell you if a number is even or odd, and if it is divisible by another integer.\n")
    
    num = int(input("Give me an integer, please!: ")) # Get number
    check = int(input("What number do you want to divide {} by?: ".format(num))) # Get divisor
    
    assert num > check, "We're only doing integer division here! The divisor you gave is larger than the dividend."
    
    if num % 4 == 0: # If mod4 is 0, the number is divisible by 4
        print(str(num) + " is a multiple of 4.")
    elif num % 2 == 0: # If mod2 is 0, the number is even
        print(str(num) + " is an even number!")
    elif num % 2 == 1: # If mod2 is 1, the number is odd
        print(str(num) + " is an odd number!")
    
    if num % check == 0: # Check if number is divisible by the given divisor
        print("And it's also divisible by " + str(check) + ".")
    elif num % check == 1:
        print("It's not divisible by " + str(check) + " though.")
        
    return
    
def list_less_than():
    '''
    Take a list and write a program that prints out all the elements of the list that are less than 5.

    Extras:
    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
    '''
    
    print("This exercise will tell you, from a predefined list of numbers, which ones are less than another number.\n")
    
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # Sample list here, can be substituted/changed
    
    num = int(input("Give me an integer, please!: "))
    
    b = [x for x in a if x < num] # List with numbers smaller than the input
    
    print("Here is the original list: ", a)
    print("From this list, {} are all less than {}.".format(b,num))
    
    return b
    
def divisors():
    '''
    Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
    '''
    
    import numpy as np
    
    print("This exercise will give you all the divisors of a number.\n")
    
    num = int(input("Give me an integer, please!: "))
    
    x = np.arange(1,num+1) # Generate an array of numbers between 1 and the input number
    
    div = []
    for n in x:
        if num % n == 0: # If modn is 0, the number is divisible by n
            div.append(n)
        else:
            continue
    
    print("{} is divisible by {}.".format(num,div))
    
    return div
    
def list_overlap():
    '''
    Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

    Extras:
    Randomly generate two lists to test this
    '''
    
    import random
    
    print("This exercise will generate two random lists of random lengths, and then tell you their intersection.\n")
    
    n1 = random.randint(1,20) # Random length of first list
    a = sorted(random.sample(range(0, 50), n1)) # First list of random length and random numbers

    n2 = random.randint(1,20) # Random length of second list
    b = sorted(random.sample(range(0, 50), n2)) # Second list of random length and random numbers
    
    #list_overlap = []
    #for i in a:
        #if i in b and i not in list_overlap: # Find intersection/overlap
            #list_overlap.append(i)
                            
    b = list(set(a))
            
    print("Here are the original lists:")
    print(a)
    print(b)
    if len(list_overlap) > 0:
        print("The intersection of these two lists is {}.".format(list_overlap))
    else:
        print("The intersection of these two lists is the null set.")
    
    return list_overlap
    
def string_list():
    '''
    Ask the user for a string and print out whether this string is a palindrome or not.
    '''
    
    print("This exercise will tell you if a word is a palindrome!\n")
    
    word = input("Input a word, and I'll check to see if it is a palindrome: ")
    
    backwards = word[::-1] # Get the word, backwards

    if word.lower() == backwards.lower(): # Compares the strings, ignoring case
        pal = True
        print("{} is a palindrome!".format(word))
    else:
        pal = False
        print("{} is not a palindrome.".format(word))
        
    return pal
    
def list_comp():
    '''
    Write one line of Python that takes a list and makes a new list that has only the even elements of this list in it.
    '''
    
    print("This exercise will tell you all the even elements of a predefined list.\n")
    
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [x for x in a if x % 2 == 0] # Get even elements
    
    print("Here is the original array: ", a)
    print("Here are the even elements from that array: ", b)
    
    return b
    
def rps():
    '''
    Make a two-player Rock-Paper-Scissors game.
    
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
        
        a = game_dict.get(player.lower())
        b = game_dict.get(CPU_rps.lower())
        
        dif = a - b
        
        print("CPU threw " + CPU_rps + ".")
    
        if dif in [-1,2]: # Compare throws to find winner
            print("Player wins!")
        elif dif in [-2,1]: # Compare throws to find winner
            print("CPU wins!")
        else: # Or tie
            print("It's a tie!")
            
        again = input("Do you want to play another game, yes or no?: ").lower()
        if again == 'yes' or again == 'y':
            continue
        else:
            print("Good game!")
            break
                
        return
                
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
                        
        count += 1 # Count how many guesses the player takes
            
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
            
    return
            
def list_overlap_v2():
    '''
    Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python.

    Extra:
    Randomly generate two lists to test this
    '''
    
    import random
    
    print("This exercise will generate two random lists of random lengths, and then tell you their intersection, using sets instead of list comprehension.\n")

    n1 = random.randint(1,20) # Random length of first list
    a = set(random.sample(range(0, 50), n1)) # First set of random length and random numbers

    n2 = random.randint(1,20) # Random length of second list
    b = set(random.sample(range(0, 50), n2)) # Second set of random length and random numbers
    
    list_overlap = sorted(list(a & b)) # Find intersection/overlap
    
    print("Here are the original lists:")
    print(a)
    print(b)
    if len(list_overlap) > 0:
        print("The intersection of these two lists is {}.".format(list_overlap))
    else:
        print("The intersection of these two lists is the null set.")
        
    return list_overlap
    
def check_prime():
    '''
    Ask the user for a number and determine whether the number is prime or not.
    '''
    
    import numpy as np
    
    print("This exercise will tell you if a number is a prime number.\n")
        
    div = divisors() # Run divisors exercise
    
    if len(div) == 2: # Prime if only divisible by 1 and itself
        print("So it is a prime number!")
    else:
        print("It's NOT a prime number.")
        
    return div
        
def first_last():
    '''
    Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
    '''
    
    print("This exercise returns an array of the first and last elements of a predefined list.\n")
    
    a = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    
    b = [a[0], a[-1]] # Create list of first and last elements
    
    print("Here is the original array: ", a)
    print("Here are the first and last elements from that array: ", b)
    
    return b
    
def fib():
    '''
    Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
    '''
    
    print("This exercise returns list of Fibonacci numbers.\n")
    
    num = int(input("How many Fibonacci numbers would you like to generate?: "))
    
    i = 1
    
    if num == 0: # Generate the first few Fibonacci numbers manually
        f = []
    elif num == 1:
        f = [1]
    elif num == 2:
        f = [1, 1]
    else: # Then just take the sum of the previous two numbers
        f = [1, 1]
        while i < (num-1):
            f.append(f[i] + f[i-1])
            i += 1
    
    print("Here are the first {} Fibonnaci numbers: {}".format(num, f))
    
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
    
    #b = []
    #for i in a:
        #if i not in b:
            #b.append(i)
                    
    b = list(set(a))
    
    print("Here is the original array: ", a)
    print("Here are the unique elements from that array: ", b)
        
    return b
    
def reverse_word():
    '''
    Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
    '''
    
    print("This exercise returns words in a sentence in the reverse order.\n")
    
    sentence = input("Write a sentence, without punctuation:\n")
        
    print(' '.join(sentence.split(' ')[::-1])) # Get the sentence, backwards
    
    return ' '.join(sentence.split(' ')[::-1])
    
def pass_gen():
    '''
    Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
    '''
    
    import string
    import random
    
    print("This exercise returns a randomly generated password.\n")
    
    length = int(input("How many characters do you want in your password? "))
    
    chars = string.ascii_letters + string.digits + string.punctuation # Which characters to choose from
    
    password = ''.join(random.choice(chars) for _ in range(length)) # Get random characters

    print("Here's your password: ", password)
    
    return password
    
def read_web_page():
    '''
    Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
    '''
    
    import requests
    from bs4 import BeautifulSoup
    
    print("This exercise returns a list of articles on the NYT homepage.\n")
    
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'} # Pretend to be a browser
    
    site = 'https://www.nytimes.com/' # Which website to scrape?
    
    response = requests.get(site,headers=headers)
    soup = BeautifulSoup(response.content, 'lxml') # Get soup
    for item in soup.select('.assetWrapper'):
        try:
            print('---------------------')
            headline = item.find('h2').get_text() # Headlines, delineated by 'h2' as of August 2020, these are all specific to the NYT homepage and probably vary from site to site
            link = item.find('a')['href'] # URLs, 'a'
            summary = item.find('p').get_text() # Brief summary, 'p'
            print(headline) # Print all this info to the terminal, a later exercise sends all of this info to a txt file
            print(link)
            print(summary)
        except Exception as e: #raise exception
            print('')
            
    return
            
def cows_bulls():
    '''
    Create a program that will play Cows and Bulls with the user.
    '''
    
    import random
    
    print("This exercise is a game of Cow-Bull.\n")
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
            break
        else: # Guess again
            cow = bull = 0
            guess = input("Guess again: ")
            
    return
            
def read_web_page_v2():
    '''
    Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

    The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

    This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.
    '''
    
    import requests
    from bs4 import BeautifulSoup
    import csv
    
    print("This exercise prints the text of an article at a predefined URL.\n")
    
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'} # Pretend to be a browser
    
    site = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture' # Which article to get?
    
    response = requests.get(site,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser') # Get soup
    
    article = soup.select('p') # Get full article text
    cleaned = []

    for i in article: # Remove containers
        temp = i.text.replace("<span>","")
        cleaned.append(temp)
        
    print(cleaned) # Print all this info to the terminal, a later exercise sends all of this info to a txt file
    
    return cleaned
            
def elem_search():
    '''
    Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns an appropriate boolean.
    '''
    
    import random
    
    print("This exercise tells you if a number is in a random list of numbers.\n")
    
    num = int(input("Give me an integer, please! (between 1 and 100): "))

    n1 = random.randint(10,20) # Random length of list
    a = sorted(random.sample(range(1, 100), n1)) # List of random length and random numbers
    
    print("Here is the original array: ", a)
    print("{} is in that array. {}".format(num, num in a))
    
    return num in a
    
def read_web_page_v3():
    '''
    Take the code from the How To Decode A Website exercise, and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

    Extras:
    Ask the user to specify the name of the output file that will be saved.
    '''

    import requests
    from bs4 import BeautifulSoup
    import csv

    print("This exercise returns the text of an article at a predefined URL to a text file named based on user input.\n")

    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'} # Pretend to be a browser
    
    site = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture' # Which article to get?
    
    response = requests.get(site,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser') # Get soup

    article = soup.select('p') # Get full article text
    cleaned = []
    
    name = input("What do you want the file to be called?: ") # Get name of output file

    for i in article: # Remove containers
        temp = i.text.replace("<span>","")
        cleaned.append(temp)

    with open(name + '.txt','w') as txt: # Write all this info to a txt file
        for line in cleaned:
            txt.write(line) # Write lines
            
    return cleaned
    
def read_file():
    '''
    Given a txt file that has a list of names, count how many of each name there are in the file, and print out the results to the screen.

    Extra:
    Instead of using the txt file from above, take this txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3.
    '''
    
    print("This exercise opens a predefined text file, reads the rows, and returns how many of each thing are in the file.\n")
    
    names_dict = {}
    with open('ref_files/nameslist.txt','r') as f: # Open the file of names
        line = f.readline() # Read line
        while line:
            line = line.strip()
            if line in names_dict:
                names_dict[line] += 1 # Add to count if name is already in the dictionary
            else:
                names_dict[line] = 1 # Start count if name isn't already in the dictionary
            line = f.readline() # Read next line
            
    print(names_dict)
    
    scenes_dict = {}
    with open('ref_files/SUNscenes.txt','r') as f:  # Open the SUN database
        line = f.readline() # Read line
        while line:
            line = line[3:-26] # Crop off the random digits at the end
            if line in scenes_dict:
                scenes_dict[line] += 1 # Add to count if image catagory is already in the dictionary
            else:
                scenes_dict[line] = 1 # Start count if image category isn't already in the dictionary
            line = f.readline() # Read next line
            
    print(scenes_dict)
    
    return names_dict, scenes_dict

def file_overlap():
    '''
    Given two txt files that have lists of numbers in them, find the numbers that are overlapping. One txt file has a list of all prime numbers under 1000, and the other txt file has a list of happy numbers up to 1000.
    '''

    print("This exercise opens two text files, containing lists of prime numbers and happy numbers, and finds the overlap of the numbers in the files.\n")
    
    primes = []
    with open('ref_files/primes.txt','r') as f: # Open the primes txt file
        line = f.readline() # Read line
        while line:
            primes.append(int(line)) # Add to the list of primes
            line = f.readline() # Read line
    primes = set(primes) # Make the list a set
    
    happy = []
    with open('ref_files/happy.txt','r') as f: # Open the happy txt files
        line = f.readline() # Read line
        while line:
            happy.append(int(line)) # Add to the list of happy numbers
            line = f.readline() # Read line
    happy = set(happy) # Make the list a set
    
    overlap = sorted(list(primes & happy)) # Find intersection/overlap
    
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
    
    return
    
def guessing_game_v2():
    '''
    In a previous exercise, we’ve written a program that "knows" a number and asks a user to guess it.

    This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

    At the end of this exchange, your program should print out how many guesses it took to get your number.
    '''

    import random
    import time

    print("This exercise will ask you to think of a number, and the CPU will try to guess the number.\n")

    print("You can type 'exit' at any time to end the game.\n")
    
    min = 1
    max = 100

    print("You have 5 seconds to think of a number between {} and {}...".format(min, max))
    
    time.sleep(5) # Wait 5 seconds
    
    count = 0
    CPU = random.randint(min,max) # Generate the first guess
    print("Okay, the CPU has the first guess: {}".format(CPU))
    
    answering = True

    while answering:
    
        ans = input("Is this the number you were thinking of? (yes, high, or low): ")
    
        if ans == 'exit': # Player can exit at any time
            print("Better luck next time, CPU!")
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
            CPU = random.randint(min,max) # Based on high guess, set new upper limit, and generate the next guess
            print("Guess: {}".format(CPU))
            answering = True
        elif ans.lower() == 'low':
            min = CPU+1
            CPU = random.randint(min,max) # Based on low guess, set new lower limit, and generate the next guess
            print("Guess: {}".format(CPU))
            answering = True
        elif ans.lower() == 'exit':
            print("Better luck next time, CPU!")
            answering = False
            
    return
            
def check_tic_tac_toe():
    '''
    We will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

    If a game of Tic Tac Toe is represented as a list of lists, like so:
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]
    where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

    Your task: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
    '''
    
    print("This exercise checks the winner of a game of tic-tac-toe.")
    
    def check_grid(grid): # Set winner to something other than None when one of the players wins
    
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
        
    # A few checks to make sure the check_grid function is getting the right answer
        
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
    
    return
    
def tic_tac_toe_input():
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
    Then ask Player 2 for their move, printing an O in that place.
    '''
    
    print("This exercise is a game of tic-tac-toe!\n")
    
    print("You can type 'exit' at any time to end the game.\n")
    
    def check_grid(grid): # Set winner to something other than None when one of the players wins

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
        
    def check_winner(grid):
        winner = check_grid(grid)
        return winner
    
    turn = 0 # Count the cells on the board that are filled to determine when the gameboard is full and the game ends
    winner = None
    game = [[0, 0, 0], # Define the empty game board
            [0, 0, 0],
            [0, 0, 0]]
            
    playing = True # Set playing to False if there is a winner or if one of the players enters 'exit'

    while playing and winner == None:
    
        if turn % 2 == 0: # Player 1 goes on even numbered turns (0,2,4...), Player 2 goes on even numbered turns (1,3,5...)
            player_turn = '1'
        else:
            player_turn = '2'
        
        if turn % 2 == 0: # Player 1 is Xs, Player 2 is Os
            player_s = 'X'
        else:
            player_s = 'O'
            
        play = input("Player {}, your turn! Where would you like to place your {} (row, col): ".format(player_turn, player_s)) # Ask for player input
        
        if play == 'exit': # Player can exit at any time
            print("Play again soon!")
            playing = False
            break
    
        col, row = play.split(',')
        col = int(col) # Get player-input column
        row.strip(' ')
        row = int(row) # Get player-input row
        
        if game[col-1][row-1] != 0: # If the player chooses a cell on the board that's already filled, let them try again
            print('\nMust select an empty space which is not occupied by a player')
            continue
        else:
            game[col-1][row-1] = str(player_s) # Otherwise, place an X or O in the cell
    
        print(game[0], '\n', game[1], '\n', game[2]) # Print the board
        
        winner = check_winner(game) # Check for a winner
        
        if turn == 8 and winner == None: # If the board is full and there is no winner, end the game
            print("No winner. Play again soon!")
            playing = False
            break
    
        turn += 1 # Increase the count of cells on the board that are filled to determine when the gameboard is full and the game ends
        
    if winner != None: # End the game when one of the players wins
        print("Player {} wins!".format(player_turn))
        
    return
        
def max_of_three():
    '''
    Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
    '''
    
    print("This exercise finds the largest of three numbers in a list, without using the max() function.")
    
    list = input("Give a list of 3 numbers, separated by commas: ")
    
    n1, n2, n3 = list.split(',') # Separate the numbers at the commas
    n1 = float(n1.strip(' '))
    n2 = float(n2.strip(' '))
    n3 = float(n3.strip(' '))
    
    max = n1 # Set initial maximum
    
    if n2 > max: # Go through other numbers and change max if greater than current max
        max = n2
    if n3 > max:
        max = n3

    print(str(max) + " is the largest number in the list you gave.")
    
    return max

def tic_tac_toe():
    '''
    This exercise is Part 4 of 4 of the Tic Tac Toe exercise series.

    The final step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend.
    '''
    
    import tic_tac_toe # Made a nicer version in a separate python file, so import from there
    
    tic_tac_toe.main()
    
def pick_word():
    '''
    This exercise is Part 1 of 3 of the Hangman exercise series.
    
    In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

    Hint: use the Python random library for picking a random word.
    '''
    
    print("This exercise opens the SOWPODS dictionary, reads the rows, and picks a random word from it.\n")
    
    import random
    
    words = []
    with open('ref_files/sowpods.txt','r') as f: # Open the SOWPODS dictionary txt files
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

   For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. Remember to stop the game when all the letters have been guessed correctly!
    '''
    
    print("This exercise is a game of hangman!\n")
    
    print("You can type 'exit' at any time to end the game.")
    
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
            
            
def hangman():
    '''
    This exercise is Part 3 of 3 of the Hangman exercise series.

    In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

    In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.

    Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

    Only let the user guess 6 times, and tell the user how many guesses they have left.
    Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
    '''
    
    print("This exercise is a game of hangman!\n")
    
    print("You can type 'exit' at any time to end the game.")
    
    letters()
    
def birthday_dictionary(birthdays=None):
    '''
    This exercise is Part 1 of 4 of the birthday data exercise series.

    For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.
    '''
    
    print("This exercise defines a dictionary of birthdays and prints one birthday, picked by the user.\n")
    
    if birthdays == None: # Function can take an input dictionary, if not, define a new one
        birthdays = {
                     "Albert Einstein": '03/14/1879',
                     "Benjamin Franklin": '01/17/1706',
                     "Ada Lovelace": '12/10/1815'
                     }
           
    print("The dictionary currently contains the birthdays of: ")
    for name in birthdays: # Print names already in the dictionary
        print(name)
        
    name = input("\nWho's birthday would you like to know?: ") # Ask which birthday to print
    
    if name in birthdays: # Print birthday
        print("{}'s birthday is {}.".format(name, birthdays[name]))
    else:
        print("Sorry, I don't know {}'s birthday.".format(name))
        
    return name, birthdays[name]

    
def birthday_json():
    '''
    This exercise is Part 2 of 4 of the birthday data exercise series.

    In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

    Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.
    '''
    
    print("This exercise lets you add to a previously defined dictionary of birthdays.\n")
    
    import json

    birthdays = dict()
    
    with open('birthdays.json', 'r') as f: # Open the birthday file
        birthdays = json.load(f) # Read data
        
    what_to_do = input("Do you want to ADD a birthday to the dictionary or GET a birthday already in the dictionary? (ADD or GET): ")
    
    if what_to_do.lower() == 'get': # Use function that lets you pick which birthday to print
        name, bday = birthday_dictionary(birthdays)
    elif what_to_do.lower() == 'add': # Add a new person and birthday to the file
        name = input("Who's birthday would you like to add?: ")
        bday = input("When is their birthday?: ")
        birthdays[name] = bday
        with open('birthdays.json', 'w') as f: # Open the birthday file
            json.dump(birthdays, f) # Write the new dictionary with the added birthday
    
    return name, bday
    
def birthday_months():
    '''
    This exercise is Part 3 of 4 of the birthday data exercise series.

    In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.
    '''
    
    print("This exercise gets the months from a previously defined dictionary of birthdays.\n")
    
    import json
    from collections import Counter
    
    month_to_string = { # Numbers corresponding to months
                        1: "January",
                        2: "February",
                        3: "March",
                        4: "April",
                        5: "May",
                        6: "June",
                        7: "July",
                        8: "August",
                        9: "September",
                        10: "October",
                        11: "November",
                        12: "December"
                        }

    birthdays = dict()
    
    with open('birthdays.json', 'r') as f: # Open the birthday file
        birthdays = json.load(f) # Read data
                       
    months = []
    for name,bday in birthdays.items():
        month = int(bday.split('/')[0]) # Remove slashes between MM/DD/YYYY
        months.append(month_to_string[month]) # Append MM to list
         
    print(Counter(months)) # Use Counter to count how many birthdays are in each month
    
    return month_to_string, Counter(months)
    
def birthday_plots():
    '''
    This exercise is Part 4 of 4 of the birthday data exercise series.

    In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.

    In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
    '''
    
    from bokeh.plotting import figure, show, output_file
    import math
    
    print("This exercise makes a histogram of the months from a previously defined dictionary of birthdays.\n")
        
    month_to_string, data = birthday_months() # Use function that counts how many birthdays are in each month
    
    x = []
    y = []
    for key,value in data.items(): # Append months as numbers (x) and counts (y)
        x.append(key)
        y.append(value)
        
    output_file("birthday_hist.html") # Name output file
        
    months = []
    for key,value in month_to_string.items(): # Append months as names
        months.append(value)
        
    p=figure(x_range=months, # Label x, y axes
             x_axis_label = 'Month',
             y_axis_label = 'Count')
    p.xaxis.major_label_orientation = math.pi/4 # Rotate tick labels
    p.vbar(x=x,top=y,width=0.75, color='blue') # Make vertical bar plot
    
    show(p) # Show plot, opens in browser

if __name__ == '__main__':

    function_dict = {'1':char_input, '2':odd_even, '3':list_less_than, '4':divisors, '5':list_overlap,
                     '6':string_list, '7':list_comp, '8':rps, '9':guessing_game, '10':list_overlap_v2,
                     '11':check_prime, '12':first_last, '13':fib, '14':remove_duplicates, '15': reverse_word,
                     '16':pass_gen, '17':read_web_page, '18':cows_bulls, '19':read_web_page_v2, '20':elem_search,
                     '21':read_web_page_v3, '22':read_file, '23':file_overlap, '24':draw_gameboard, '25':guessing_game_v2,
                     '26':check_tic_tac_toe, '27':tic_tac_toe_input, '28':max_of_three, '29': tic_tac_toe, '30':pick_word,
                     '31':letters, '32':hangman, '33':birthday_dictionary, '34':birthday_json, '35':birthday_months,
                     '36':birthday_plots} # What exercise corresponds to each function

    print("Go to practicepython.org to see which function number corresponds to which exercise.")
    exercise = input("Which exercise do you want to run? (1-36): ")
    print("Exercise " + exercise)

    function_dict[exercise]() # Runs exercise
    
