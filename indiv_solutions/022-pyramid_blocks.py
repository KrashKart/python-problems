# working in indiv_solutions/022-pyramid_blocks_working.png
def pyramid_blocks(n, m, h):
    return n * m * h + (n + m) * h * (h - 1) // 2 + h * (h - 1) * (2 * h - 1) // 6