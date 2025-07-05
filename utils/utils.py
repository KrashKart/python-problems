def return_cards(ace_last=True):
    if ace_last:
        return ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    else:
        return ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

def minNone(a, b):
    if not a and not b:
        raise ValueError("Parameters cannot be None!")
    elif not b:
        return a
    elif not a:
        return b
    return min(a, b)

def maxNone(a, b):
    if not a and not b:
        raise ValueError("Parameters cannot be None!")
    elif not b:
        return a
    elif not a:
        return b
    return max(a, b)