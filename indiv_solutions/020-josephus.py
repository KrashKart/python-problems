def josephus(n, k):
    curr, tally, counter = list(range(1, n + 1)), list(), -1
    while curr:
        counter += k
        counter %= len(curr)
        tally.append(curr[counter])
        curr.pop(counter)
        counter -= 1
    return tally