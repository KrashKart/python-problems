def group_and_skip(n, out, ins):
    tally = []
    while n:
        tally.append(n % out)
        n = n // out * ins
    return tally