def remove_after_kth(items, k=1):
    if k == 0:
        return []
    ref, tally = {}, []
    for i in items:
        ref[i] = ref.get(i, 0)
        if ref[i] < k:
            tally.append(i)
            ref[i] += 1
    return tally