import random

class Blackjack:
    def __init__(self):
        self.cards = range(1, 53)
        self.shuffle()
        self.deal()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        self.player = [None, None]
        self.dealer = [None, None]

        for i in xrange(4):
            if i % 2:
                self.player[i/2] = self.cards.pop()
            else:
                self.dealer[i/2] = self.cards.pop()

if __name__ == "__main__":
    """
    This is testing only, this module is intended
    to be imported.
    """
    bj = Blackjack()
    print bj.player
    print bj.dealer
