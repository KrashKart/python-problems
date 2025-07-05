def collapse_intervals(items):
    if not items or len(items) == 1:
        return "" if not items else items[0]
    tally = []
    start = items[0]
    for i in range(1, len(items) + 1):
        if i == len(items) or items[i] != items[i - 1] + 1:
            tally.append(str(start) if start == items[i - 1] else f"{start}-{items[i - 1]}")
            if i != len(items):
                start = items[i]

    return ",".join(tally)