def is_cyclops(n):
    if not n:
        return True
    digits, num_zeros, zero_pos = 0, 0, 0
    while n > 0:
        digits += 1
        if n % 10 == 0:
            num_zeros += 1
            zero_pos = digits
        n //= 10
    return num_zeros == 1 and digits % 2 == 1 and zero_pos == digits // 2 + 1