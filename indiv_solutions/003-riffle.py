def riffle(items, out=True):
    res = []
    half = len(items) // 2
    for i in range(half):
        res.extend([items[i], items[i+half]] if out else [items[i+half], items[i]])
    return res