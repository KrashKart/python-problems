def count_growlers(animals):
    cds, growls = [0, 0], 0
    lefts, rights = ["cat", "dog"], ["tac", "god"]
    for i in range(len(animals)):
        if animals[i] in lefts:
            growls += 1 if cds[1] > cds[0] else 0
        cds[lefts.index(animals[i]) if animals[i] in lefts else rights.index(animals[i])] += 1
            
    cds = [0, 0]
    for i in range(len(animals) - 1, -1, -1):
        if animals[i] in rights:
            growls += 1 if cds[1] > cds[0] else 0
        cds[lefts.index(animals[i]) if animals[i] in lefts else rights.index(animals[i])] += 1
    
    return growls 