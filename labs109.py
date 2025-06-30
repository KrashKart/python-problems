import utils

# def ryerson_letter_grade(pct):
#     if pct < 50:
#         return "F"
#     elif pct > 89:
#         return "A+"
#     elif pct > 84:
#         return "A"
#     elif pct > 79:
#         return "A-"
    
#     tens = pct // 10
#     ones = pct % 10
#     modifier = ""
#     if ones > 6:
#         modifier = "+"
#     elif ones < 3:
#         modifier = "-"
#     return "DCBA"[tens - 5] + modifier

# def is_ascending(items):
#     for i in range(1, len(items)):
#         if items[i-1] >= items[i]:
#             return False
#     return True

# def riffle(items, out=True):
#     res = []
#     half = len(items) // 2
#     for i in range(half):
#         res.extend([items[i], items[i+half]] if out else [items[i+half], items[i]])
#     return res

# def only_odd_digits(n):
#     while n > 0:
#         ones = n % 10
#         if ones % 2 == 0:
#             return False
#         n //= 10
#     return True

# def is_cyclops(n):
#     if not n:
#         return True
#     digits, num_zeros, zero_pos = 0, 0, 0
#     while n > 0:
#         digits += 1
#         if n % 10 == 0:
#             num_zeros += 1
#             zero_pos = digits
#         n //= 10
#     return num_zeros == 1 and digits % 2 == 1 and zero_pos == digits // 2 + 1

# def domino_cycle(tiles):
#     for i in range(1, len(tiles)):
#         if tiles[i-1][1] != tiles[i][0]:
#             return False
#     return not tiles or tiles[-1][1] == tiles[0][0]

# def colour_trio(colours):
#     def mix(a, b):
#         if a == b:
#             return a
#         elif a + b in ("ry", "yr"):
#             return "b"
#         elif a + b in ("rb", "br"):
#             return "y"
#         else:
#             return "r"
    
#     curr, temp = colours, ""
#     while len(curr) > 1:
#         for i in range(len(curr) - 1):
#             temp += mix(curr[i], curr[i+1])
#         curr = temp
#         temp = ""
#     return curr

# def count_dominators(items):
#     max_elem = -float("inf")
#     tally = 0
#     for i in range(len(items) - 1, -1, -1):
#         if items[i] > max_elem:
#             tally += 1
#         max_elem = max(max_elem, items[i])
#     return tally

# def extract_increasing(digits):
#     running_max = -float("inf")
#     temp, res = 0, []
#     for i in digits:
#         temp = temp * 10 + int(i)
#         if temp > running_max:
#             res.append(temp)
#             running_max = temp
#             temp = 0
#     return res

# def words_with_letters(words, letters):
#     def is_subsequence(word, letters):
#         idx = 0
#         for i in word:
#             if i == letters[idx]:
#                 idx += 1
#                 if idx == len(letters):
#                     return True
#         return False
    
#     return list(filter(lambda x: is_subsequence(x, letters), words))

# def taxi_zum_zum(moves):
#     curr = 0 + 0j
#     heading = 0 + 1j
#     for m in moves:
#         if m == "L":
#             heading *= 1j
#         elif m == "R":
#             heading *= -1j
#         else:
#             curr += heading
#     return (int(curr.real), int(curr.imag))

# def give_change(amount, coins):
#     curr, tally = 0, []
#     while amount:
#         if amount < coins[curr]:
#             curr += 1
#         else:
#             left = amount % coins[curr]
#             tally += amount // coins[curr] * [coins[curr]]
#             amount = left
#     return tally

# def safe_squares_rooks(n, rooks):
#     row_set = set()
#     col_set = set()
#     safe = set(range(n))
#     for r in rooks:
#         row_set.add(r[0])
#         col_set.add(r[1])
    
#     return len(safe - row_set) * len(safe - col_set)

# def words_with_given_shape(words, shape):
#     def has_shape(word, shape):
#         if len(word) != len(shape) + 1:
#             return False
#         for i in range(len(shape)):
#             if shape[i] == 0 and ord(word[i]) != ord(word[i+1]):
#                 return False
#             elif shape[i] * ord(word[i]) >= shape[i] * ord(word[i+1]) and shape[i] != 0:
#                 return False
#         return True
#     return list(filter(lambda x: has_shape(x, shape), words))

# def is_left_handed(pips):
#     flips = 0
#     for i in range(len(pips)):
#         if pips[i] > 3:
#             flips += 1
#             pips[i] = 7 - pips[i]
    
#     is_left = pips in [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
#     return is_left if flips % 2 == 0 else not is_left

# def winning_card(cards, trump=None):
#     ref = utils.return_cards()

#     if not trump:
#         trump = cards[0][1]
    
#     highest = ()
#     for c in cards:
#         if not highest:
#             highest = c
#         elif c[1] == highest[1] and ref.index(c[0]) > ref.index(highest[0]):
#             highest = c
#         elif c[1] == trump and highest[1] != trump:
#             highest = c
#     return highest

# def knight_jump(knight, start, end):
#     diff = tuple(map(lambda x: abs(x[0] - x[1]), zip(start, end)))
#     return knight == tuple(sorted(diff, reverse=True))

# def seven_zero(n):
#     def gen(digits, ends_zero):
#         while True:
#             if ends_zero:
#                 for k in range(1, digits):
#                     yield int("7" * k + "0" * (digits - k))
#             else:
#                 yield int("7" * digits)
#             digits += 1
    
#     for num in gen(len(str(n)), n % 2  == 0 or n % 5 == 0):
#         if num % n == 0:
#             return num

# def can_balance(items):
#     length = len(items)
#     for i in range(length):
#         tally = 0
#         for j in range(length):
#             tally += items[j] * (j - i)
#         if not tally:
#             return i
#     return -1

# def josephus(n, k):
#     curr, tally, counter = list(range(1, n + 1)), list(), -1
#     while curr:
#         counter += k
#         counter %= len(curr)
#         tally.append(curr[counter])
#         curr.pop(counter)
#         counter -= 1
#     return tally

# def group_and_skip(n, out, ins):
#     tally = []
#     while n:
#         tally.append(n % out)
#         n = n // out * ins
#     return tally

# # working in indiv_solutions/022-pyramid_blocks_working.png
# def pyramid_blocks(n, m, h):
#     return n * m * h + (n + m) * h * (h - 1) // 2 + h * (h - 1) * (2 * h - 1) // 6

# def count_growlers(animals):
#     cds, growls = [0, 0], 0
#     lefts, rights = ["cat", "dog"], ["tac", "god"]
#     for i in range(len(animals)):
#         if animals[i] in lefts:
#             growls += 1 if cds[1] > cds[0] else 0
#         cds[lefts.index(animals[i]) if animals[i] in lefts else rights.index(animals[i])] += 1
            
#     cds = [0, 0]
#     for i in range(len(animals) - 1, -1, -1):
#         if animals[i] in rights:
#             growls += 1 if cds[1] > cds[0] else 0
#         cds[lefts.index(animals[i]) if animals[i] in lefts else rights.index(animals[i])] += 1
    
#     return growls 

# def bulgarian_solitaire(piles, k):
#     target, steps = list(range(1, k + 1)), 0
#     while sorted(piles) != target:
#         new_pile = len(piles)
#         piles = list(filter(lambda x: x != 1, piles))
#         piles = list(map(lambda x: x - 1, piles))
#         piles.append(new_pile)
#         steps += 1
#     return steps

# def scylla_or_charybdis(moves, n):
#     k, minlen, mink = 1, len(moves), 1
#     while k < len(moves):
#         temp = moves[k - 1::k]
#         curr = 0
#         for i in range(len(temp)):
#             curr += 1 if temp[i] == "+" else -1
#             if abs(curr) >= n and i < minlen:
#                 minlen, mink = i, k
#                 break
#         k += 1
#     return mink

# def arithmetic_progression(items):
#     n = len(items)
#     dp = [dict() for _ in range(n)]
#     best = (items[0], 0, 1)
#     for i in range(1, n):
#         for j in range(i):
#             stride = items[i] - items[j]
#             length = dp[j].get(stride, 1) + 1
#             dp[i][stride] = max(dp[j].get(stride, 0), length)

#             start = items[i] - (length - 1) * stride
#             current = (start, stride, length)

#             # Compare with best
#             if (length > best[2] or (length == best[2] and start < best[0]) or (length == best[2] and start == best[0] and stride < best[1])):
#                 best = current

#     return best
