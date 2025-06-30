def collect_numbers(perm):
    n = len(perm)
    inv = list(range(n))
    for i in range(n):
        inv[perm[i]] = i
    rounds = 1
    for i in range(1, n):
        if inv[i] < inv[i-1]:
            rounds += 1
    return rounds