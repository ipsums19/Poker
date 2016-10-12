
def poker(hands):
    return max(hands, key = hand_rank)

def card_ranks(hand):
    "Return a list of the ranks"
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

def hand_rank(hand):
    "return a value of the hand"
    ranks = card_ranks(hand)
    if straigth(tanks) and flush(hand):      #straight flush
        return (8, max(ranks))
    elif kind(4,ranks):                      #poker
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):  #full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                        #flush
        return (5, ranks)
    elif straight(ranks):                    #straight
        return (4, max(ranks))
    elif kind(3, ranks):                     #3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                    #2pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                     #2 of a kind
        return (1, kind(2, ranks), ranks)
    else:                                    #nothing
        return (0, ranks)
