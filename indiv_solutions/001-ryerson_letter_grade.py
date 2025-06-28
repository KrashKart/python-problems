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