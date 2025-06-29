def knight_jump(knight, start, end):
    diff = tuple(map(lambda x: abs(x[0] - x[1]), zip(start, end)))
    return knight == tuple(sorted(diff, reverse=True))