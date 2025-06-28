def domino_cycle(tiles):
    for i in range(1, len(tiles)):
        if tiles[i-1][1] != tiles[i][0]:
            return False
    return not tiles or tiles[-1][1] == tiles[0][0]