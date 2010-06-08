import random

FACES = {
    1: 'A',
    11: 'J',
    12: 'Q',
    13: 'K'
}

class BlackjackHand(list):
    """
    A Blackjack hand.

    This is basically just a list, except that it prints out like a hand of
    blackjack and adds some blackjack-specific members.
    """

    def score(self):
        """
        Calculates the blackjack score for a given hand. Properly takes
        Aces and face cards into account.
        """
        score = 0
        aces = 0
        for card in self:
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

    def _string_list(self):
        card_strings = []
        for card in self:
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
            value = FACES[value] if value in FACES else value
            card_strings.append(suit + unicode(value))
        return card_strings

    def hidden(self):
        """
        Returns a string representation that hides the first card. This is
        useful for showing what the dealer has.
        """
        strings = self._string_list()
        strings[0] = "**"
        return u", ".join(strings)

    def __str__(self):
        return u", ".join(self._string_list())


class Blackjack(object):
    """
    Class to play a round of blackjack.
    """

    """
    status - can be one of 'playing', 'house', 'player', 'push', or 'blackjack',
             It's up to the user to check the status before continuing
             to play the game. If the status is not "playing", no function
             can be expected to work correctly. The game is over when the
             status changes from "playing"

             If the status is 'playing', the game should continue

             If the status is 'house', then the house won

             If the status is 'player', then the player won

             If the status is 'push', then the dealer and player tied

             If the status is 'blackjack', then the player hit blackjack
    """
    status = 'playing'

    def __init__(self):
        """
        Start a round of blackjack. This shuffles and deals the cards.

        Please read the notes on 'status' to understand how the game progresses
        """
        self.deck = range(52)
        self.shuffle()
        self.deal()

    def shuffle(self):
        """
        Shuffles the cards. This is done automatically when the
        class is created.
        """
        random.shuffle(self.deck)

    def deal(self):
        """
        Deal the cards. This is done automatically when the class
        is created.
        """
        self.player = BlackjackHand()
        self.dealer = BlackjackHand()

        for i in xrange(4):
            if i % 2:
                self.player.append(self.deck.pop())
            else:
                self.dealer.append(self.deck.pop())
        self._check_blackjack()

    def hit(self):
        """
        Indicates that the player wants to hit. Will draw a card off the
        deck and add it to the player's hand.
        """
        self.player.append(self.deck.pop())
        if self.player.score() > 21:
            self._house_win()
            return

        self._dealer_round()

    def stand(self):
        """
        Indicates that the player wants to stand. This effectively ends the
        round. The dealer will hit as necessary until its score is > 21 and
        then the round will end. Be sure to check the status after calling
        this.
        """
        while (self._dealer_round()):
            pass
        if self.status == 'playing':
            player_score = self.player.score()
            dealer_score = self.dealer.score()
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
        if self.dealer.score() < 17:
            self.dealer.append(self.deck.pop())
            if self.dealer.score() > 21:
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

    def _check_blackjack(self):
        pscore = self.player.score()
        dscore = self.dealer.score()
        if pscore == 21 and dscore != 21:
            self.status = 'blackjack'
        elif pscore == 21 and dscore == 21:
            self.status = 'push'
        elif dscore == 21:
            self.status = 'house'


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

    print "Player: ", bj.player.score()
    print unicode(bj.player)
    print "Dealer: ", bj.dealer.score()
    print unicode(bj.dealer)
    print bj.status
