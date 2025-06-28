def count_dominators(items):
    max_elem = -float("inf")
    tally = 0
    for i in range(len(items) - 1, -1, -1):
        if items[i] > max_elem:
            tally += 1
        max_elem = max(max_elem, items[i])
    return tally