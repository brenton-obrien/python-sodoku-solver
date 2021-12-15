# Automatic Sodoku Solver created by Brenton O'Brien
# This command line based program will take an unsolved sodoku board (represented as a nested list with zeros as the unsolved squares) as input,
# and will output all possible solutions

# Imports
import os
import copy

# This is the unsolved Sodoku board.
# It is a representation of the 9x9 board. Each prefilled number should be filled with an integer,
# I have opted to use single space strings to represent empty squares instead of zeros as it makes
# it easier to see the progress of the program whilst it is solving.
# This is my example board used for testing, edit this board to test for your own solutions

grid = [[6, 8, ' ', 9, ' ', ' ', 4, ' ', ' '],
        [' ', ' ', 3, ' ', 8, ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 2, 5, ' ', 6, 8, ' '],
        [2, 6, ' ', 3, ' ', 5, 8, ' ', ' '],
        [5, 1, ' ', ' ', ' ', 6, ' ', 4, ' '],
        [' ', ' ', 4, ' ', 9, ' ', ' ', 5, 6],
        [3, ' ', 7, 1, ' ', ' ', 5, ' ', ' '],
        [' ', 9, ' ', 5, 3, 8, 7, ' ', ' '],
        [' ', 5, 6, ' ', ' ', ' ', ' ', ' ', ' ']]

# Saves a copy of the grid so that a 'before' and 'after' can be displayed
unsolved_grid = copy.deepcopy(grid)


# Neat way to display the board to the user
def print_board(grid):
    print('')
    print(f'   {grid[0][0]} {grid[0][1]} {grid[0][2]}  |  {grid[0][3]} {grid[0][4]} {grid[0][5]}  |  {grid[0][6]} {grid[0][7]} {grid[0][8]} ')
    print(f'   {grid[1][0]} {grid[1][1]} {grid[1][2]}  |  {grid[1][3]} {grid[1][4]} {grid[1][5]}  |  {grid[1][6]} {grid[1][7]} {grid[1][8]} ')
    print(f'   {grid[2][0]} {grid[2][1]} {grid[2][2]}  |  {grid[2][3]} {grid[2][4]} {grid[2][5]}  |  {grid[2][6]} {grid[2][7]} {grid[2][8]} ')
    print(' - - - - - - - - - - - - - - - ')
    print(f'   {grid[3][0]} {grid[3][1]} {grid[3][2]}  |  {grid[3][3]} {grid[3][4]} {grid[3][5]}  |  {grid[3][6]} {grid[3][7]} {grid[3][8]} ')
    print(f'   {grid[4][0]} {grid[4][1]} {grid[4][2]}  |  {grid[4][3]} {grid[4][4]} {grid[4][5]}  |  {grid[4][6]} {grid[4][7]} {grid[4][8]} ')
    print(f'   {grid[5][0]} {grid[5][1]} {grid[5][2]}  |  {grid[5][3]} {grid[5][4]} {grid[5][5]}  |  {grid[5][6]} {grid[5][7]} {grid[5][8]} ')
    print(' - - - - - - - - - - - - - - - ')
    print(f'   {grid[6][0]} {grid[6][1]} {grid[6][2]}  |  {grid[6][3]} {grid[6][4]} {grid[6][5]}  |  {grid[6][6]} {grid[6][7]} {grid[6][8]} ')
    print(f'   {grid[7][0]} {grid[7][1]} {grid[7][2]}  |  {grid[7][3]} {grid[7][4]} {grid[7][5]}  |  {grid[7][6]} {grid[7][7]} {grid[7][8]} ')
    print(f'   {grid[8][0]} {grid[8][1]} {grid[8][2]}  |  {grid[8][3]} {grid[8][4]} {grid[8][5]}  |  {grid[8][6]} {grid[8][7]} {grid[8][8]} ')
    print('')


# Clears the terminal
def cls():
    os.system('cls')


# Check to see if a certain number can be placed into a square, returns False if it cannot
def check_possible_number(row, column, number):
    global grid

    # Checks if number already exists in the row
    for i in range(9):
        if grid[row][i] == number:
            return False

    # Checks if number already exists in the column
    for i in range(9):
        if grid[i][column] == number:
            return False

    # Checks if number is in the 3x3 square
    # Create variables that divide the grid into 9 3x3 zones, to creates an 'origin point' to check each zone
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3

    # Loop through each square in the 3x3 zone
    for i in range(3):
        for j in range(3):

            if grid[y0 + i][x0 + j] == number:
                return False

    return True


# Checks every free square (the zero's) and will input a valid guess. Will recursively rerun the function until a solution is found if there is one.
def recursive_solver():
    global grid
    screen_refresh()

    # Checks every square in the grid that is a zero
    for row in range(9):
        for column in range(9):
            if grid[row][column] == ' ':

                # Uses integers from 1 to 9 as guesses
                for number in range(1, 10):

                    # Runs the check function and see if it returns true
                    if check_possible_number(row, column, number):
                        # If it does then update the grid with the valid number
                        grid[row][column] = number

                        # Continue solving
                        recursive_solver()

                        # Make the square 0 if the program gets stuck
                        grid[row][column] = ' '

                return

    # Once the solving is completed, clear the screen, reprint title, unsolved board, and the now completed board.
    cls()
    print("\nSodoku Solver - Brenton O'Brien")
    print('\nOriginal: ')
    print_board(unsolved_grid)
    print('\nSolving complete: ')
    print_board(grid)
    input('\nPress ENTER to find more solutions (if any): \n<ENTER>')


# Clears the screen, reprints the title, reprints unsolved board, and prints each new version of the board as it is being solved.
def screen_refresh():
    cls()
    print("\nSodoku Solver - Brenton O'Brien")
    print('\nOriginal: ')
    print_board(unsolved_grid)
    print('\nSolving...')
    print_board(grid)


# Initial printing of the title and unsolved board. Input allows the user to view the board prior to it being solved.
print("\nSodoku Solver - Brenton O'Brien")
print('\nOriginal: ')
print_board(unsolved_grid)
input('\nPress ENTER to begin solving: \n<ENTER>')
recursive_solver()

# Stops the program from closing after the program has exhausted all possible solutions. Informs the user prior to closing, and asks them to acknowledge.
input('\n\nNo other solutions found.\n\nPress ENTER to EXIT:\n<ENTER>')