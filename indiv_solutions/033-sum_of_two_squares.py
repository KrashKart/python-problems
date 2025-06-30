def sum_of_two_squares(n):
    i, j = 1, round(n ** 0.5) + 1
    while i <= j:
        total = i ** 2 + j ** 2
        if total == n:
            return (j, i)
        elif total < n:
            i += 1
        else:
            j -= 1
    return None