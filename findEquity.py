from card import Card as c 
from deck import Deck as d
from findWinner import * 
import multiprocessing as mp
import numpy as np 



def getTotalEquity(flop1, flop2, flop3, turn, river, hand1, hand2, finalDeck):
		board = [finalDeck[int(flop1)], finalDeck[int(flop2)],finalDeck[int(flop3)], finalDeck[int(turn)], finalDeck[int(river)]]
		board1 = board[:]
		board2 = board[:]
		for h in hand1: board1.append(h)
		for h in hand2: board2.append(h)
		winner = findWinner(board1, board2)
		if winner == 1: return 1 
		if winner == 0: return 0
		if winner == 2: return -1 

def generateAllCombos():#1712304
	res = np.zeros((1712305, 5))
	idx = 0 
	for a in range(0,48):
		for b in range(a+1, 48):
			for c in range(b+1, 48):
				for d in range(c+1, 48):
					for e in range(d+1, 48):
						idx +=  1 
						res[idx, ] = np.array([a,b,c,d,e])
	return res 


def findEquityHelper(hand1, hand2, finalDeck, res):
	results = []
	pool = mp.Pool(mp.cpu_count())
	results = pool.starmap_async(getTotalEquity, [(a, b, c, d, e, hand1, hand2, finalDeck) for a, b, c, d, e in res]).get()
	pool.close()
	return results 

def findEquity(hand1, hand2):
	hand1 = [c('A', 's'), c('K', 'c')]
	hand2 = [c('5', 'd'), c('5', 'h')]
	deck = d()
	for card in hand1:
		deck.remove(card) 
	for card in hand2:
		deck.remove(card)
	finalDeck = deck.getDeck()
	r = generateAllCombos()
	total = findEquityHelper(hand1, hand2, finalDeck, r)
	tie, eq, tot = 0, 0, 0
	for t in total:
		if t == 0: tie += 1 
		if t == 1: eq += 1 
		tot += 1 
	totalEq = (eq + 0.5*tie)/tot
	return totalEq 
