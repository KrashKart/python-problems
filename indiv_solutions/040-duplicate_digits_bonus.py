def duplicate_digit_bonus(n):
    curr_digit, length, score = -1, 0, 0
    multiplier = 2
    while n > 0:
        if curr_digit != -1 and curr_digit != n % 10:
            score += 10 ** (length - 2) * multiplier if length > 1 else 0
            length = 0
            multiplier = max(multiplier - 1, 1)
        
        curr_digit = n % 10
        length += 1
        n //= 10

    score += 10 ** (length - 2) * multiplier if length > 1 else 0
    return score