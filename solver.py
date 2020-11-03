#create the solver
from card import Card as c 
from findEquity import *
from generateTotalRange import *
def getUpdatedCallingRange(bb_range, bu_shoving_range, pot_size):
	#calculate every hand in bb_range vs bu_shoving range
	# see if it hass enough equity
	# if so, set that hand in bb-range to true 

	for h in range(len(bb_range)):
		c1, c2, freq, profit = bb_range[h]
		if freq == 6: hand = [c(c1, 's'), c(c2, 'c')]
		if freq == 12: hand = [c(c1, 's'), c(c2, 'c')]
		if freq == 4: hand = [c(c1, 's'), c(c2, 's')]
		EV = 0
		for jam in range(len(bu_shoving_range)):
			jam1, jam2, freq2, profit2 = bu_shoving_range[jam]
			if not profit2: continue 
			totalFreq = freq * freq2 
			if freq2 == 6: jam_hand = [c(jam1, 's'), c(jam2, 'c')]
			if freq2 == 12: jam_hand = [c(jam1, 's'), c(jam2, 'c')]
			if freq2 == 4: jam_hand = [c(jam1, 's'), c(jam2, 's')] 
			equity = findEquity(hand, jam_hand)
			EV += (freq * (equity*pot_size - pot_size/2))

		if EV < 0: bb_range[h][3] = False 
		else: bb_range[h][3] = True 


	return bb_range

def getUpdatedJammingRange(bu_range, bb_calling_range, pot_size):
	# set for loop through rnage vs range
	# if folded - add 1 to total EV 
	# if called - find 10 - x% of 20 (or total) and multiply by frequency 
	# get total EV - see if positive or negative 
	for h in range(len(bu_range)):
		c1, c2, freq, profit = bb_range[h]
		if freq == 6: hand = [c(c1, 's'), c(c2, 'c')]
		if freq == 12: hand = [c(c1, 's'), c(c2, 'c')]
		if freq == 4: hand = [c(c1, 's'), c(c2, 's')]
		EV = 0
		for call in range(len(bb_calling_range)):
			call1, call2, freq2, profit2 = bb_calling_range[call]
			if not profit2:
				EV += 1 
				continue 
			totalFreq = freq * freq2 
			if freq2 == 6: call_hand = [c(call1, 's'), c(call2, 'c')]
			if freq2 == 12: call_hand = [c(call1, 's'), c(call2, 'c')]
			if freq2 == 4: call_hand = [c(call1, 's'), c(call2, 's')] 
			equity = findEquity(hand, call_hand)
			EV += (freq * (equity*pot_size - pot_size/2))

		if EV < 0: bu_range[h][3] = False 
		else: bu_range[h][3] = True 
	return bu_range

if __name__ == "__main__":
	total = eval(input("Enter effective stack: "))
	odds = (total-1)/(2*total)
	iterations = 10

	bb_total = generateTotalRange()
	bu_total = generateTotalRange()
	# range - array with four columns - card1, card2, freq, true/false 

	bu_cur = bu_total[:]
	for _ in range(iterations):
		bb_cur = getUpdatedCallingRange(bb_total[:], bu_cur, total*2)
		bu_cur = getUpdatedJammingRange(bu_total[:], bb_cur, total*2)

	print("Button's jamming range: ")

	for r in bu_cur:
		if r[3]: print(r)

	print("****************")
	print("Big Blind's calling range: ")

	for r in bb_cur:
		if r[3]: print(r)


