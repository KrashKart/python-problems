def leibniz(heads, positions):
    prev = [heads[0]]
    for i in heads:
        curr = [i]
        for j in range(len(prev)):
            curr.append(prev[j] - curr[-1])
        prev = curr
    return [curr[c] for c in positions]