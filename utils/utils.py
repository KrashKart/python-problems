def return_cards(ace_last=True):
    if ace_last:
        return ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    else:
        return ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

def minNone(a, b):
    if a is None and b is None:
        raise ValueError("Parameters cannot be None!")
    elif b is None:
        return a
    elif a is None:
        return b
    return min(a, b)

def maxNone(a, b):
    if a is None and b is None:
        raise ValueError("Parameters cannot be None!")
    elif b is None:
        return a
    elif a is None:
        return b
    return max(a, b)