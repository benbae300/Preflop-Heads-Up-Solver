
# ideas for efficiency:
# set an input as cardCounter, so we only have to run it once
# only make it check for the actual values if values clash, otherwise waste of time
# create a one reverse array to cut down on reversing time
# when comparing different hand classes, can have more efficient 'break' clauses

########## OTHER HELPER FUNCTIONS ##########
def getDict(board):
    cardCounter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    suits = {'c': [0, []], 'd': [0, []], 'h': [0, []], 's': [0, []]}
    reverse = {}
    for card in board:
        cardCounter[card.getValue()] += 1
        suits[card.suit][0] += 1
        suits[card.suit][1].append(card.getValue())
    for key, value in cardCounter.items():
        reverse.setdefault(value, list()).append(key)
    sortedKeys = sorted(cardCounter.keys(), reverse=True)
    return cardCounter, suits, reverse, sortedKeys

def isStraight(board):
    i = 1
    while i < 5:
        if board[i] - board[i-1] != 1: return False
        i += 1
    return True

def isStraightFlush(board):
    if board[4] == "14" and board[0] == '2' and board[1] == '3' and board[2] == '4' and board[3] == '5': return True
    return isStraight(board)

########## CHECKING FUNCTIONS ##########
def checkStraightFlush(suits):
    if checkFlush(suits):
        for key in suits:
            if suits[key][0] >= 5:
                flushList = suits[key][1]
        for i in range(0, len(flushList)-4):
            if isStraightFlush(flushList[i:i+5]): return True
    return False
def checkQuads(cardCounter):return True if 4 in cardCounter.values() else False
def checkBoat(cardCounter, reverse):
    if (3 in cardCounter.values() and 2 in cardCounter.values()): return True
    if (3 in reverse and len(reverse[3]) > 1): return True
    return False
def checkFlush(suits):
    for key in suits:
        if suits[key][0] >= 5: return True
    return False
def checkStraight(cardCounter):
    straightList = list()
    for val in cardCounter:
        if cardCounter[val] > 0: straightList.append(val)
    if '2' in straightList and '3' in straightList and '4' in straightList and '5' in straightList and '14' in straightList: return True
    for idx in range(0, len(straightList) - 4):
        if isStraight(straightList[idx:idx + 5]): return True
    return False

def checkTrips(cardCounter): return True if 3 in cardCounter.values() else False
def checkTwoPair(reverse): return True if 2 in reverse and len(reverse[2]) >= 2 else False
def checkPair(cardCounter): return True if 2 in cardCounter.values() else False


########## COMPARISON FUNCTIONS ##########
def compareStraightFlush(suits):
    # check for 5
    suitKey = ''
    for key in suits:
        if suits[key][0] >= 5: suitKey = key
    board = suits[suitKey][1]
    if board[-1] == "14" and board[0] == '2' and board[1] == '3' and board[2] == '4' and board[3] == '5': return 5
    if suits[suitKey][0] == 5: return board[-1]
    if suits[suitKey][0] == 6:
        if(isStraightFlush(board[1:6])): return board[-1]
        else: return board[4]
    if suits[suitKey][0] == 7:
        if(isStraightFlush(board[2:7])): return board[-1]
        elif(isStraightFlush(board[1:6])): return board[5]
        else: return board[4]
def compareQuads(cardCounter, sortedKeys):
    res = [-1, -1]
    for key in cardCounter:
        if cardCounter[key] == 4:
            res[0] = key
            break
    for key in sortedKeys:
        if key != res[0] and cardCounter[key] > 0:
            res[1] = key
            break
    return res
###########
def compareBoat(cardCounter, reverse, sortedKeys):
    res = [-1, -1]
    if(3 in reverse and len(reverse[3]) > 1):
        for key in sortedKeys:
            if(cardCounter[key] == 3):
                if(res[0] == -1): res[0] = key
                else: res[1] = key
            if(res[-1] != -1): break
        return res
    if( 3 in cardCounter.values() and 2 in cardCounter.values()):
        for key in sortedKeys:
            if(cardCounter[key] == 3 and res[0] == -1): res[0] = key
            if(cardCounter[key] == 2 and res[1] == -1): res[1] = key
            if(res[-1] != -1): break
        return res
###########
def compareFlush(suits):
    for key in suits:
        if suits[key][0] == 5: return suits[key][1]
        if suits[key][0] == 6: return suits[key][1][1:]
        if suits[key][0] == 7: return suits[key][1][2:]
    return None
########### update the calling functions
def compareStraight(cardCounter):
    straightList = list()
    finalCard = None
    for val in cardCounter:
        if cardCounter[val] > 0: straightList.append(val)
    for idx in range(0, len(straightList) - 4):
        if isStraight(straightList[idx:idx+5]): finalCard= straightList[idx]
    return finalCard if finalCard else 5
###########
def compareTrips(cardCounter, sortedKeys):
    res = [-1, -1, -1]
    for key in cardCounter:
        if cardCounter[key] == 3:
            res[0] = key
            break
    for key in sortedKeys:
        if key != res[0] and cardCounter[key] > 0:
            if (res[1] == -1): res[1] = key
            else: res[2] = key
        if res[-1] != -1: break
    return res
###########
def compareTwoPair(cardCounter, sortedKeys):
    res = [-1, -1, -1]
    for key in sortedKeys:
        if cardCounter[key] == 2:
            if res[0] == -1: res[0] = key
            else: res[1] = key
        if -1 not in res[0:2]: break
    for key in sortedKeys:
        if key not in res and cardCounter[key] > 0:
            res[2] = key
        if res[-1] != -1: break
    return res
###########
def comparePair(cardCounter, sortedKeys):
    res = [-1, -1, -1, -1]
    for key in cardCounter:
        if cardCounter[key] == 2:
            res[0] = key
            break
    j = 1
    for key in sortedKeys:
        if key not in res and cardCounter[key] > 0:
            res[j] = key
            j += 1
        if(j == 4): break
    return res
###########
def compareUnpair(cardCounter, sortedKeys):
    res, i = [-1, -1, -1, -1, -1], 0
    for key in sortedKeys:
        if cardCounter[key] > 0:
            res[i] = key
            i += 1
        if res[-1] != -1: break
    return res


def getHandRank(board, cardCounter, suits, reverse):
    # will have two ranks, one is for hand rank, next will be if hand rank is same
    if checkStraightFlush(suits): return 9
    elif checkQuads(cardCounter): return 8
    elif checkBoat(cardCounter, reverse): return 7
    elif checkFlush(suits): return 6
    elif checkStraight(cardCounter): return 5
    elif checkTrips(cardCounter): return 4
    elif checkTwoPair(reverse): return 3
    elif checkPair(cardCounter): return 2
    else: return 1

def compareSameHand(handVal, A, ACardCounter, ASuits, AReverse, ASortedKeys, B, BCardCounter, BSuits, BReverse, BSortedKeys):
    if handVal == 9:
        AVal, BVal = compareStraightFlush(ASuits), compareStraightFlush(BSuits)
        return 1 if AVal > BVal else (2 if BVal > AVal else 0)
    elif handVal == 8:
        AVal, BVal = compareQuads(ACardCounter, ASortedKeys), compareQuads(BCardCounter, BSortedKeys)
        return 1 if AVal > BVal else (2 if BVal > AVal else 0)
    elif handVal == 7:
        AVal, BVal = compareBoat(ACardCounter, AReverse, ASortedKeys), compareBoat(BCardCounter, BReverse, BSortedKeys)
        return 1 if AVal > BVal else (2 if BVal > AVal else 0)
    elif handVal == 6:
        AVal, BVal = compareFlush(ASuits), compareFlush(BSuits)
        return 1 if AVal > BVal else (2 if BVal > AVal else 0)
    elif handVal == 5:
        AVal, BVal = compareStraight(ACardCounter), compareStraight(BCardCounter)
        return 1 if AVal > BVal else (2 if BVal > AVal else 0)
    elif handVal == 4:
        AVal, BVal = compareTrips(ACardCounter, ASortedKeys), compareTrips(BCardCounter, BSortedKeys)
        return 1 if AVal > BVal else (2 if BVal > AVal else 0)
    elif handVal == 3:
        AVal, BVal = compareTwoPair(ACardCounter, ASortedKeys), compareTwoPair(BCardCounter, BSortedKeys)
        return 1 if AVal > BVal else (2 if BVal > AVal else 0)
    elif handVal == 2:
        AVal, BVal = comparePair(ACardCounter, ASortedKeys), comparePair(BCardCounter, BSortedKeys)
        return 1 if AVal > BVal else (2 if BVal > AVal else 0)
    else:
        AVal, BVal = compareUnpair(ACardCounter, ASortedKeys), compareUnpair(BCardCounter, BSortedKeys)
        return 1 if AVal > BVal else (2 if BVal > AVal else 0)

def findWinner(A, B):
    A.sort(key = lambda x: x.getValue())
    B.sort(key=lambda x: x.getValue())
    ACardCounter, Asuits, Areverse, ASortedKeys = getDict(A)
    BCardCounter, Bsuits, Breverse, BSortedKeys = getDict(B)
    ARank = getHandRank(A, ACardCounter, Asuits, Areverse)
    BRank = getHandRank(B, BCardCounter, Bsuits, Breverse)
    return 1 if ARank > BRank else (2 if BRank > ARank else compareSameHand(ARank, A, ACardCounter, Asuits, Areverse, ASortedKeys,
                                                                            B,BCardCounter, Bsuits, Breverse, BSortedKeys ))



