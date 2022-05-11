def clear_at(val: int, position: int):
    mask = ~(1 << position)
    return val & mask


def clear_from_to(val: int, start: int, stop: int):
    delta = stop - start + 1
    mask = ~(~(1 << delta) << start)
    print(format(mask, "08b"))
    return val & mask


def insert_into(larger: int, smaller: int, start: int, stop: int) -> int:
    smaller_size = len(f"{smaller:b}")
    shift = stop - smaller_size - 1 + start
    # shift = stop - start + 1
    # smaller_size = len(f"{smaller:b}")
    # delta = stop - smaller_size
    shifted_smaller = smaller << shift
    return larger | shifted_smaller
