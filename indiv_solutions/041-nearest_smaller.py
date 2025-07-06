def nearest_smaller(items):
    tally = []
    for i in range(len(items)):
        left = right = None
        for j in range(i - 1, -1, -1):
            if items[i] > items[j]:
                left = items[j]
                break
        for k in range(i + 1, len(items)):
            if items[i] > items[k]:
                right = items[k]
                break

        if left is not None and right is not None:
            if i - j == k - i:
                tally.append(min(left, right))
            else:
                tally.append(left if k - i > i - j else right)
        elif left is None and right is None:
            tally.append(items[i])
        else:
            tally.append(left if left is not None else right)
    return tally
