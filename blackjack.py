import random

class Blackjack:
    def __init__(self):
        self.cards = range(1, 53)
        self.shuffle()
        self.deal()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        self.player = (self.cards[0], self.cards[2])
        self.dealer = (self.cards[1], self.cards[3])


if __name__ == "__main__":
    """
    This is testing only, this module is intended
    to be imported.
    """
    bj = Blackjack()
    print bj.player
    print bj.dealer
