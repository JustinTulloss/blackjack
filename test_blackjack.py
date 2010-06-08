from blackjack import BlackjackHand, Blackjack

# BlackjackHand Tests
def test_4_aces():
    h = BlackjackHand([0, 13, 26, 39])
    assert h.score() == 14

def test_blackjack_score():
    h = BlackjackHand([0, 12])
    assert h.score() == 21

def test_ace_face_num():
    h = BlackjackHand([0, 11, 25, 28])
    assert h.score() == 24

def test_spades():
    h = BlackjackHand([0])
    assert u"\u2660" in unicode(h)

def test_hearts():
    h = BlackjackHand([14])
    assert u"\u2665" in unicode(h)

def test_clubs():
    h = BlackjackHand([28])
    assert u"\u2663" in unicode(h)

def test_diamonds():
    h = BlackjackHand([43])
    assert u"\u2666" in unicode(h)

def test_face():
    h = BlackjackHand([0])
    assert u"A" in unicode(h)

# Blackjack tests
def test_deal():
    bj = Blackjack()
    assert len(bj.dealer) == 2
    assert len(bj.player) == 2
    assert bj.dealer[0] not in bj.deck
    assert bj.player[1] not in bj.deck

def test_blackjack():
    bj = Blackjack()
    bj.status = 'playing'
    bj.dealer = BlackjackHand([1,2])
    bj.player = BlackjackHand([0,11])
    bj._check_blackjack()
    assert bj.status == 'blackjack'

def test_dealer_blackjack():
    bj = Blackjack()
    bj.status = 'playing'
    bj.player = BlackjackHand([1,2])
    bj.dealer = BlackjackHand([0,11])
    bj._check_blackjack()
    assert bj.status == 'house'

def test_blackjack_push():
    bj = Blackjack()
    bj.status = 'playing'
    bj.player = BlackjackHand([13, 12])
    bj.dealer = BlackjackHand([0,11])
    bj._check_blackjack()
    assert bj.status == 'push'

def test_hit():
    bj = Blackjack()
    bj.player = BlackjackHand([0, 11])
    bj.dealer = BlackjackHand([2,3])
    bj.hit()
    assert len(bj.player) == 3, "Player didn't hit"
    assert len(bj.dealer) == 3, "Dealer didn't hit"
    assert bj.dealer[2] not in bj.deck
    assert bj.player[2] not in bj.deck

def test_stand():
    bj = Blackjack()
    bj.player = BlackjackHand([0, 11])
    bj.dealer = BlackjackHand([2,3])
    bj.stand()
    assert len(bj.player) == 2 , "Player didn't stand"
    assert len(bj.dealer) >= 3, "Dealer didn't hit"

