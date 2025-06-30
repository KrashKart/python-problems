def arithmetic_progression(items):
    n = len(items)
    dp = [dict() for _ in range(n)]
    best = (items[0], 0, 1)
    for i in range(1, n):
        for j in range(i):
            stride = items[i] - items[j]
            length = dp[j].get(stride, 1) + 1
            dp[i][stride] = max(dp[j].get(stride, 0), length)

            start = items[i] - (length - 1) * stride
            current = (start, stride, length)

            # Compare with best
            if (length > best[2] or (length == best[2] and start < best[0]) or (length == best[2] and start == best[0] and stride < best[1])):
                best = current

    return best