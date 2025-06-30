def bulgarian_solitaire(piles, k):
    target, steps = list(range(1, k + 1)), 0
    while sorted(piles) != target:
        new_pile = len(piles)
        piles = list(filter(lambda x: x != 1, piles))
        piles = list(map(lambda x: x - 1, piles))
        piles.append(new_pile)
        steps += 1
    return steps