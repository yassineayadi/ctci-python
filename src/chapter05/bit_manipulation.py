def get_bit(val: int, position: int):
    mask = 1 << position
    return (mask & val) != 0


def set_bit(val: int, position: int):
    mask = 1 << position
    return mask | val


def clear_bit(val: int, position: int):
    mask = ~(1 << position)
    return mask & val

def clear_bits_to(val: int, stop: int):
    mask = (1 << stop) - 1
    return mask & val

def clear_bits_from(val: int, start: int):
    mask = (1 << start)
    return mask & val

def update_bit(val: int, bit: bool, position: int):
    bit = int(bit)
    mask = bit << position
    return mask | val
