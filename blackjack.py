import random

class Blackjack:
    def __init__(self):
        self.deck = range(1, 53)
        self.shuffle()
        self.deal()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.player = [None, None]
        self.dealer = [None, None]

        for i in xrange(4):
            if i % 2:
                self.player[i/2] = self.deck.pop()
            else:
                self.dealer[(i-1)/2] = self.deck.pop()

if __name__ == "__main__":
    """
    This is testing only, this module is intended
    to be imported.
    """
    bj = Blackjack()
    print bj.player
    print bj.dealer
