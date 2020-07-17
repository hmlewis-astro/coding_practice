'''
File name: pythonpractice.py
Author: Hannah Lewis
Date created: 07/17/2020
Date last modified: 07/17/2020
Python Version: 3.7

These are a bunch of silly practice problems from practicepython.org. Exercises 1-10 are included here.
'''

def main():
    for arg in sys.argv[1:]:
        


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
    
    year, _, _, _, _ = map(int, time.strftime("%Y %m %d %H %M").split())
    year_100 = year - age + 100
    
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
    
    if num % 4 == 0:
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
    
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
    num = int(input("Give me an integer, please!: "))
    
    b = [x for x in a if x <= num]
    print(b)
    
def divisors():
    '''
    Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
    '''
    
    import numpy as np
    
    num = int(input("Give me an integer, please!: "))
    
    x = np.arange(1,num)
    
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
    
    n1 = random.randint(1,20)
    a = random.sample(range(0, 50), n1)

    n2 = random.randint(1,20)
    b = random.sample(range(0, 50), n2)
    
    list_overlap = []
    for i in a:
        if i in b and i not in list_overlap:
            list_overlap.append(i)
    
    print(list_overlap)
    
        
if __name__ == '__main__':

    main()
