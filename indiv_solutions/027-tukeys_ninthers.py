def tukeys_ninthers(items):
    while len(items) > 1:
        temp = []
        for i in range(0, len(items), 3):
            a, b, c = items[i:i+3]
            if a <= b <= c or c <= b <= a:
                temp.append(b)
            elif b <= a <= c or c <= a <= b:
                temp.append(a)
            else:
                temp.append(c)
        items = temp
    return items[0]
