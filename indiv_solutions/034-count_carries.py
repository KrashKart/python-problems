def count_carries(a, b):
    tally, carry = 0, 0
    while a > 0 or b > 0:
        if a % 10 + b % 10 + carry > 9:
            tally += 1
            carry = 1
        else:
            carry = 0
        a, b = a // 10, b // 10

    return tally