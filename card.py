class Card():
    def __init__(self, val, suit):
        self.value = val
        self.suit = suit

    def __repr__(self):
        return '{}{}'.format(self.value)

    def getValue(self):
        cardValue = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7
                     , '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        if self.value not in cardValue: return None
        return cardValue[self.value]

