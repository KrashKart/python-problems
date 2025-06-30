def verify_betweenness(perm, constraints):
    n = len(perm)
    inv = list(range(n))
    for i in range(n):
        inv[perm[i]] = i
    
    for c in constraints:
        if not (inv[c[0]] < inv[c[1]] < inv[c[2]] or inv[c[0]] > inv[c[1]] > inv[c[2]]):
            return False
    return True