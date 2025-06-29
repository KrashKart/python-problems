def give_change(amount, coins):
    curr, tally = 0, []
    while amount:
        if amount < coins[curr]:
            curr += 1
        else:
            left = amount % coins[curr]
            tally += amount // coins[curr] * [coins[curr]]
            amount = left
    return tally