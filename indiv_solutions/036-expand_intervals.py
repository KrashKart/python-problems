def expand_intervals(intervals):
    tally = []
    if intervals:
        intervals = intervals.split(",")
        for i in intervals:
            if "-" not in i:
                tally.append(int(i))
            else:
                start, end = i.split("-")
                for j in range(int(start), int(end) + 1):
                    tally.append(j)
    return tally