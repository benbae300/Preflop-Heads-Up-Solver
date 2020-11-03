def generatePartialRange(card_dict, max_range, idx, totalRange):
	cur = max_range - 1 
	for i in range(2, max_range):
		if i == cur: 
			totalRange[idx] = [card_dict[cur], card_dict[cur], 6, True]
			idx += 1 
		else:
			totalRange[idx] = [card_dict[cur], card_dict[i], 12, True]
			totalRange[idx+1] = [card_dict[cur], card_dict[i], 4, True]
			idx += 2

	return idx, totalRange


def generateTotalRange():
	#card1, card2, freq, True/False
	totalRange = [[] for i in range(169)]
	card_dict = {2:'2', 3:'3',4:'4',5:'5',6:'6',7:'7',8:'8', 9:'9',10:'T',11:'J',12:'Q',13:'K',14:'A'}
	idx = 0 
	idx, totalRange = generatePartialRange(card_dict, 15, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 14, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 13, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 12, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 11, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 10, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 9, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 8, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 7, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 6, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 5, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 4, idx, totalRange)
	idx, totalRange = generatePartialRange(card_dict, 3, idx, totalRange)
	return totalRange 







