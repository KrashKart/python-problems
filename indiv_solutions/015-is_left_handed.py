def is_left_handed(pips):
    flips = 0
    for i in range(len(pips)):
        if pips[i] > 3:
            flips += 1
            pips[i] = 7 - pips[i]
    
    is_left = pips in [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    return is_left if flips % 2 == 0 else not is_left