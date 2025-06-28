def only_odd_digits(n):
    while n > 0:
        ones = n % 10
        if ones % 2 == 0:
            return False
        n //= 10
    return True