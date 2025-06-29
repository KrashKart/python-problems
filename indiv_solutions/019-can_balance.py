def can_balance(items):
    length = len(items)
    for i in range(length):
        tally = 0
        for j in range(length):
            tally += items[j] * (j - i)
        if not tally:
            return i
    return -1