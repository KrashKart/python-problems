def seven_zero(n):
    def gen(digits, ends_zero):
        while True:
            if ends_zero:
                for k in range(1, digits):
                    yield int("7" * k + "0" * (digits - k))
            else:
                yield int("7" * digits)
            digits += 1
    
    for num in gen(len(str(n)), n % 2  == 0 or n % 5 == 0):
        if num % n == 0:
            return num