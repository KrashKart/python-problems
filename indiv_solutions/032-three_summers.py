def three_summers(items, goal):
    def two_summers(i, j, goal):
        while i < j:
            total = items[i] + items[j]
            if total == goal:
                return True
            elif total < goal:
                i += 1
            else:
                j -= 1
        return False

    for i in range(len(items) - 2):
        if two_summers(i + 1, len(items) - 1, goal - items[i]):
            return True
    return False