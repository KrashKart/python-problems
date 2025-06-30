def crag_score(dice):
    sorted_dice = sorted(dice)
    a, b, c = sorted_dice
    if (a == b or b == c) and a + b + c == 13:
        return 50
    elif a + b + c == 13:
        return 26
    elif a == b == c:
        return 25
    elif sorted_dice in [[1,2,3], [4,5,6], [1,3,5], [2,4,6]]:
        return 20
    else:
        return max([a + b if a == b else 0, b + c if b == c else 0, c])