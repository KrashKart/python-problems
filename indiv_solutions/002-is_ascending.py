def is_ascending(items):
    for i in range(1, len(items)):
        if items[i-1] >= items[i]:
            return False
    return True