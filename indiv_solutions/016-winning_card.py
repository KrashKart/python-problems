import utils
def winning_card(cards, trump=None):
    ref = utils.return_cards()

    if not trump:
        trump = cards[0][1]
    
    highest = ()
    for c in cards:
        if not highest:
            highest = c
        elif c[1] == highest[1] and ref.index(c[0]) > ref.index(highest[0]):
            highest = c
        elif c[1] == trump and highest[1] != trump:
            highest = c
    return highest