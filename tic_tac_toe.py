'''
File name: pythonpractice.py
Author: Hannah Lewis
Date created: 07/17/2020
Date last modified: 08/02/2020
Python Version: 3.7
'''
    
def draw_gameboard(size, grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
    '''
    This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
    
    This function draws the gameboard.
    '''
    
    if size == None: # If no size given, ask how large of a gameboard the user wants
        size = int(input("How large do you want your gameboard to be?: "))

    print(' ---' * size) # Print top boundary line
    for x in range(size):
        row = []
        for y in range(size): # Get grid values and convert them to Xs and Os
            if grid[x][y] == 1:
                symb = 'X'
            elif grid[x][y] == 2:
                symb = 'O'
            else:
                symb = ' '
            row.append(symb)
        print('| ' + ' | '.join(map(str, row)) + ' |') # Print filled cells with boundary lines for columns
        print(' ---' * size) # Print boundary lines between rows
            
def check_tic_tac_toe(grid):
    '''
    This exercise is Part 2 of 4 of the Tic Tac Toe exercise series.
    
    This function checks the winner of a game of tic-tac-toe.
    '''
        
    def check_grid(grid):
    
        for x in range(0,3): # Define what a win looks like in a row
            row = set([grid[x][0],grid[x][1],grid[x][2]])
            if len(row) == 1 and grid[x][0] != 0:
                return grid[x][0]

        for x in range(0,3): # Define what a win looks like in a column
            column = set([grid[0][x],grid[1][x],grid[2][x]])
            if len(column) == 1 and grid[0][x] != 0:
                return grid[0][x]

        diag1 = set([grid[0][0],grid[1][1],grid[2][2]]) # Define what a win looks like on a diagonal
        diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
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
                      
    # A handful of sample input grids to check that the check_grid function is written correctly
    assert check_grid(winner_is_1) == 1, "Got the wrong winner"
    assert check_grid(winner_is_also_1) == 1, "Got the wrong winner"
    assert check_grid(winner_is_2) == 2, "Got the wrong winner"
    assert check_grid(no_winner) == None, "Got the wrong winner"
    assert check_grid(also_no_winner) == None, "Got the wrong winner"
    assert check_grid(first_move) == None, "Got the wrong winner"
                       
    return check_grid(grid)
    
def tic_tac_toe_input():
    '''
    This exercise is Part 3 of 4 of the Tic Tac Toe exercise series.
    
    This function gets input plays from 2 players and determines when there is a winner or when the game is over.
    '''
        
    def check_winner(grid): # Set winner to something other than None when one of the players wins
        winner = check_tic_tac_toe(grid)
        return winner
    
    turn = 0 # Count the cells on the board that are filled to determine when the gameboard is full and the game ends
    winner = None
    game_n = [[0, 0, 0], # Define the empty game board
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
    
        col, row = play.split(',')
        col = int(col) # Get player-input column
        row.strip(' ')
        row = int(row) # Get player-input row
        
        if game_n[col-1][row-1] != 0: # If the player chooses a cell on the board that's already filled, let them try again
            print('\nMust select an empty space which is not occupied by a player')
            continue
        else:
            game_n[col-1][row-1] = int(player_turn) # Otherwise, place an X or O in the cell
    
        draw_gameboard(3, game_n) # Draw the board

        winner = check_winner(game_n) # Check for a winner
        
        if turn == 8 and winner == None: # If the board is full and there is no winner, end the game
            print("No winner. Play again soon!")
            playing = False
    
        turn += 1 # Increase the count of cells on the board that are filled to determine when the gameboard is full and the game ends
        
    if winner != None: # End the game when one of the players wins
        print("Player {} wins! Play again soon!".format(player_turn))
        
def main():
    '''
    This exercise is Part 4 of 4 of the Tic Tac Toe exercise series.

    The final step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend.
    '''
    
    print("Ready to play a game of tic-tac-toe?")
    print("You can type 'exit' at any time to end the game.")
    print("Here's your game board:")
    
    draw_gameboard(3) # Draw the empty board
    
    tic_tac_toe_input() # Play the game!


if __name__ == '__main__':

    main() # Runs exercise
    
