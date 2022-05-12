def clear_odds(number: int):
    size = len(f"{number:b}")
    mask = 0
    for i in range(size):
        if i % 2 == 0:
            mask <<= 1
            mask |= 1
        else:
            mask <<= 1
    mask = mask << 1 if size % 2 == 0 else mask
    return number & mask


def clear_pairs(number: int):
    size = len(f"{number:b}")
    mask = 0
    for i in range(size):
        if i % 2 == 0:
            mask <<= 1
            mask |= 1
        else:
            mask <<= 1
    if not size % 2 == 0:
        mask <<= 1
        mask |= 1
    return number & mask


def swap_odds_and_pairs(number: int):
    odds = clear_pairs(number) >> 1
    pairs = clear_odds(number) << 1
    return odds | pairs
