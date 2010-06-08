from blackjack import BlackjackHand, Blackjack

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
