def safe_squares_rooks(n, rooks):
    row_set = set()
    col_set = set()
    safe = set(range(n))
    for r in rooks:
        row_set.add(r[0])
        col_set.add(r[1])
    
    return len(safe - row_set) * len(safe - col_set)