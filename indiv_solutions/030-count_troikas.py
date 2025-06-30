def count_troikas(items):
    tally = dict()
    for i in range(len(items)):
        temp = tally.get(items[i], [])
        temp.append(i)
        tally[items[i]] = temp
    
    troikas = 0
    for _, v in tally.items():
        if len(v) > 2:
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    if 2 * v[j] - v[i] in v:
                        troikas += 1
    return troikas