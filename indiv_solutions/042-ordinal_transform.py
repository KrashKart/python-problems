def ordinal_transform(seed, i):
    while len(seed) <= i:
        ref, temp = {}, []
        for s in seed:
            ref[s] = ref.get(s, 0) + 1
            temp.append(ref[s])
        
        seed.extend(temp)
    return seed[i]