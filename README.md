# Preflop Heads-Up Push/Fold Solver
This allows you to calculate the optimal pushing range AND calling range for a heads up scenario. Input the effective stack (and you can also edit the number of iterations to run) and this solver uses multiprocessing to quickly calculate the optimal shoving and calling strategies, trying to reach Nash Equilibria as closely as possible. 
Some explanations of the files: 
- findWinner calculates the winner of the hand given two 7 card holdings (2 hole cards + 5 cards on the board)
- findEquity finds the equity of two hands 
- generateTotalRange returns as a list all possible combinations of hands and their frequencies of which they appear in a range 
- solver is the main code to run the solver that compares 2 sub-optimal rangess and continues to run them until Nash is reached

# What is Preflop? Heads-Up? Push/Fold?
Simply put, 'heads up' poker is simply a 1 on 1 variant where instead of multiple players, there are only two players 'butting heads.' Preflop is the action regarding your two private cards, i.e. the round of betting before the players see the board. Finally, push/fold implies a very binary decision- a 'going all in or folding' strategy. 

# When do we need this solved strategy?
Though it seems niche, this situation is not as unique as you may think. Being short stacked (not having many chips) means that there is hardly any room for post flop navigation, and any additional chips gained a surprisingly large % of your stack. This means that it becomes higher EV to turn to a jam/fold strategy than your traditional preflop moves. A general tip would be that the shorter you are, the more incentivized you are to jam your hand rather than a normal raise. There are quite a few situations where knowing a solved jam/fold strategy would be helpful, mainly  in tournament blind versus blind spots or in Sit N Gos (fast tournaments usually sitting only 2, 3, or 6 players with a winner-takes-all format). In fact, I created this solver specifically for that purpose; I realized my game was weak in 3 man Sit N Gos, and using this solver has actually proved more consistent results!
