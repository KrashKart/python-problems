def brussels_choice_step(n, mink, maxk):
    s = str(n)
    l = len(s)
    tally = []

    for k in range(mink, maxk + 1):
        for i in range(l - k + 1):
            m = int(s[i:i + k])

            double_m = str(2 * m)
            half_m = str(m // 2) if m % 2 == 0 else None

            for new_sub in [double_m, half_m]:
                if new_sub is None:
                    continue

                new_num_str = s[:i] + new_sub + s[i + k:]
                tally.append(int(new_num_str))
    
    return sorted(tally)