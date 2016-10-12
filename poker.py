
def poker(hands):
    return allmax(hands, key = hand_rank)

def allmax(hands, key = None):
    "Return all max"
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

def straight(ranks):
    "True if a 5-card straigth"
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "True if 5-card same suit"
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def card_ranks(hand):
    "Return a list of the ranks"
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    pair = kin(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def hand_rank(hand):
    "return a value of the hand"
    ranks = card_ranks(hand)
    if straigth(ranks) and flush(hand):      #straight flush
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
