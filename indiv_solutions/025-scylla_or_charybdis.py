def scylla_or_charybdis(moves, n):
    k, minlen, mink = 1, len(moves), 1
    while k < len(moves):
        temp = moves[k - 1::k]
        curr = 0
        for i in range(len(temp)):
            curr += 1 if temp[i] == "+" else -1
            if abs(curr) >= n and i < minlen:
                minlen, mink = i, k
                break
        k += 1
    return mink