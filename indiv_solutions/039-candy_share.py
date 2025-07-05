def candy_share(candies):
    rounds = 0
    n = len(candies)
    prev = candies[::]
    while True:
        if not list(filter(lambda x: x > 1, candies)):
            return rounds
        
        for i in range(n):
            if prev[i] > 1:
                candies[(i + 1) % n] += 1
                candies[(i - 1) % n] += 1
                candies[i] -= 2
        rounds += 1
        prev = candies[::]