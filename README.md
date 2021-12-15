# python-sodoku-solver
A simple command line sodoku puzzle solver written in python. The program is able to return all possible solutions for a puzzle.

You need to edit the source code to change what board the program will solve.

The unsolved board in the source sode will look like this:

grid = [[6, 8, ' ', 9, ' ', ' ', 4, ' ', ' '],
        [' ', ' ', 3, ' ', 8, ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 2, 5, ' ', 6, 8, ' '],
        [2, 6, ' ', 3, ' ', 5, 8, ' ', ' '],
        [5, 1, ' ', ' ', ' ', 6, ' ', 4, ' '],
        [' ', ' ', 4, ' ', 9, ' ', ' ', 5, 6],
        [3, ' ', 7, 1, ' ', ' ', 5, ' ', ' '],
        [' ', 9, ' ', 5, 3, 8, 7, ' ', ' '],
        [' ', 5, 6, ' ', ' ', ' ', ' ', ' ', ' ']]
        
This is the board I used during testing as it has several solutions to it.
Prefilled numbers are represented by integers: 1, 2, 3 etc, and unsolved squares are represented by single spaced strings: ' '.

Once you have edited the source code, run the program and hit enter to begin solving once you are happy the 'unsolved board' is correct.
The program will return the first solution (if there is any), and ask the user if they want to keep searching.
The program will return all subsequent solutions one by one until there is no more, at which point it will inform the user and wait to be closed.

Thanks for checking this out, if you have any feedback let me know, or if you got something out of it please leave a star.
Thankyou!
-Brenton
