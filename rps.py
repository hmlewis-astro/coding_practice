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
    Make a two-player Rock-Paper-Scissors game.

    I'm actually going to make this a one-player vs. CPU game with random throws from the CPU

    Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
    '''
    
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
            
        #TODO: keep track of how many games Player vs. CPU has won
            
        return

if __name__ == '__main__':

    print("Ready to play Rock, Paper, Scissors?")

    main() # Runs exercise
    
