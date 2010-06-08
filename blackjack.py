import random

face_map = {
    1: 'A',
    11: 'J',
    12: 'Q',
    13: 'K'
}

class Blackjack:
    """
    Class to play a round of blackjack.
    """
    def __init__(self):
        self.deck = range(52)
        self.shuffle()
        self.deal()
        self.status = 'playing'

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

    def score(self, hand):
        score = 0
        aces = 0
        for card in hand:
            value = (card % 13) + 1
            if value == 1:
                score += 11
                aces += 1
            else:
                score += min(10, value)

        while score > 21 and aces:
            score -= 10
            aces -= 1

        return score

    def hit(self):
        self.player.append(self.deck.pop())
        if self.score(self.player) > 21:
            self._house_win()
            return

        self._dealer_round()

    def stand(self):
        while (self._dealer_round()):
            pass
        if self.status == 'playing':
            player_score = self.score(self.player)
            dealer_score = self.score(self.dealer)
            if player_score == dealer_score:
                self._push()
            elif player_score > dealer_score:
                self._player_win()
            else:
                self._house_win()

    def _dealer_round(self):
        """
        Deals the dealer another card. Returns True if the dealer might
        want another card in the future.
        """
        if self.score(self.dealer) < 17:
            self.dealer.append(self.deck.pop())
            if self.score(self.dealer) > 21:
                self._player_win()
                return False
            else:
                return True
        else:
            return False

    def _player_win(self):
        self.status = 'player'

    def _house_win(self):
        self.status = 'house'

    def _push(self):
        self.status = 'push'

    def getString(self, card):
        suit_num = card/13
        if suit_num < 1:
            suit = u"\u2660"
        elif suit_num < 2:
            suit = u"\u2665"
        elif suit_num < 3:
            suit = u"\u2663"
        else:
            suit = u"\u2666"

        value = (card % 13) + 1
        value = face_map[value] if value in face_map else value
        return suit + unicode(value)

if __name__ == "__main__":
    """
    This is testing only, this module is intended
    to be imported.
    """
    bj = Blackjack()
    bj.dealer
    bj.hit()
    if bj.status == 'playing':
        bj.stand()

    print "Player: ", bj.score(bj.player)
    for card in bj.player:
        print bj.getString(card)
    print "Dealer: ", bj.score(bj.dealer)
    for card in bj.dealer:
        print bj.getString(card)
    print bj.status
