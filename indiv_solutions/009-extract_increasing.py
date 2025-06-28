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