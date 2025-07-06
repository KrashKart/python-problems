def oware_move(board, house):
    n = len(board)
    i, offset = 1, 0
    while i < board[house] + 1 + offset:
        if (house + i) % n != house:
            board[(house + i) % n] += 1
        else:
            offset += 1
        i += 1

    i -= 1
    board[house] = 0
    while True:
        if 1 < board[(house + i) % n] < 4 and (house + i) % n >= n // 2:
            board[(house + i) % n] = 0
            i -= 1
        else:
            break
    return board