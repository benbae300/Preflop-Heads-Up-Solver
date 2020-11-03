from card import Card as crd

class Deck():
    def __init__(self):
        num = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        suit = ['c', 'h', 'd', 's']
        self.deck = []
        for n in num:
            for s in suit:
                self.deck.append(crd(n, s))

    def remove(self, card):
        for c in self.deck:
            if(c.value == card.value and c.suit == card.suit): self.deck.remove(c)

    def getDeck(self):
        return self.deck
