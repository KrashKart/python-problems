def taxi_zum_zum(moves):
    curr = 0 + 0j
    heading = 0 + 1j
    for m in moves:
        if m == "L":
            heading *= 1j
        elif m == "R":
            heading *= -1j
        else:
            curr += heading
    return (int(curr.real), int(curr.imag))