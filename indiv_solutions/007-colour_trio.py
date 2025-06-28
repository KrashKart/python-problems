def colour_trio(colours):
    def mix(a, b):
        if a == b:
            return a
        elif a + b in ("ry", "yr"):
            return "b"
        elif a + b in ("rb", "br"):
            return "y"
        else:
            return "r"
    
    cols = {"r", "y", "b"}
    def mix_alternate(a, b):
        if a == b:
            return a
        return (cols - {a, b}).pop()
    
    curr, temp = colours, ""
    while len(curr) > 1:
        for i in range(len(curr) - 1):
            temp += mix(curr[i], curr[i+1])
        curr = temp
        temp = ""
    return curr

