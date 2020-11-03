# Preflop-Heads-Up-Solver
This allows you to calculate the optimal pushing range AND calling range for a heads up scenario. Input the effective stack (and you can also edit the number of iterations to run) and this solver uses multiprocessing to quickly calculate the optimal shoving and calling strategies, trying to reach Nash Equilibria as closely as possible. 
Some explanations of the files: 
- findWinner calculates the winner of the hand given two 7 card holdings (2 hole cards + 5 cards on the board)
- findEquity finds the equity of two hands 
- generateTotalRange returns as a list all possible combinations of hands and their frequencies of which they appear in a range 
- solver is the main code to run the solver that compares 2 sub-optimal rangess and continues to run them until Nash is reached
