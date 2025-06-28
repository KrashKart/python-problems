def ryerson_letter_grade(pct):
    if pct < 50:
        return "F"
    elif pct > 89:
        return "A+"
    elif pct > 84:
        return "A"
    elif pct > 79:
        return "A-"
    
    tens = pct // 10
    ones = pct % 10
    modifier = ""
    if ones > 6:
        modifier = "+"
    elif ones < 3:
        modifier = "-"
    return "DCBA"[tens - 5] + modifier

def is_ascending(items):
    for i in range(1, len(items)):
        if items[i-1] >= items[i]:
            return False
    return True

def riffle(items, out=True):
    res = []
    half = len(items) // 2
    for i in range(half):
        res.extend([items[i], items[i+half]] if out else [items[i+half], items[i]])
    return res

def only_odd_digits(n):
    while n > 0:
        ones = n % 10
        if ones % 2 == 0:
            return False
        n //= 10
    return True

def is_cyclops(n):
    if not n:
        return True
    digits, num_zeros, zero_pos = 0, 0, 0
    while n > 0:
        digits += 1
        if n % 10 == 0:
            num_zeros += 1
            zero_pos = digits
        n //= 10
    return num_zeros == 1 and digits % 2 == 1 and zero_pos == digits // 2 + 1

def domino_cycle(tiles):
    for i in range(1, len(tiles)):
        if tiles[i-1][1] != tiles[i][0]:
            return False
    return not tiles or tiles[-1][1] == tiles[0][0]

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
    
    curr, temp = colours, ""
    while len(curr) > 1:
        for i in range(len(curr) - 1):
            temp += mix(curr[i], curr[i+1])
        curr = temp
        temp = ""
    return curr

def count_dominators(items):
    max_elem = -float("inf")
    tally = 0
    for i in range(len(items) - 1, -1, -1):
        if items[i] > max_elem:
            tally += 1
        max_elem = max(max_elem, items[i])
    return tally

def extract_increasing(digits):
    running_max = -float("inf")
    temp, res = 0, []
    for i in digits:
        temp = temp * 10 + int(i)
        if temp > running_max:
            res.append(temp)
            running_max = temp
            temp = 0
    return res

def words_with_letters(words, letters):
    def is_subsequence(word, letters):
        idx = 0
        for i in word:
            if i == letters[idx]:
                idx += 1
                if idx == len(letters):
                    return True
        return False
    
    return list(filter(lambda x: is_subsequence(x, letters), words))