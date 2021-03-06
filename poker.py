import random

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Return n random hands"
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

def hand_percentages(n=50000):
    counts = [0]*9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print 100.*counts[i]/n

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
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

count_ranking = {(5,):10, (4,1):7, (3,2):6, (3, 1, 1):3, (2, 2, 1):2,
                (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}

def hand_rank(hand):
    "return a value of the hand"
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return max(count_ranking[counts], 4*straight + 5*flush), ranks

def group(items):
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse = True)

def unzip(pairs): return zip(*pairs)
