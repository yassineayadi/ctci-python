def set_at(val: int, position: int):
    mask = 1 << position
    return val | mask


def clear_at(val: int, position: int):
    mask = ~(1 << position)
    return val & mask


def clear_to(val: int, position: int):
    mask = ~((1 << position) - 1)
    return val & mask


def fill_with_1s(val: int, position: int):
    mask = (1 << position) - 1
    return val | mask


def fill_with_0s(val: int, position: int):
    return clear_to(val, position)


def count_1s(val: int, stop: int) -> int:
    binary = f"{val:b}"
    idx = len(binary)
    count = 0
    while idx > (idx - stop):
        current = int(binary[idx - 1])
        if current == 1:
            count += 1
        idx -= 1
    return count


def count_0s(val: int, stop: int) -> int:
    binary = f"{val:b}"
    idx, count = len(binary), 0

    while idx > (len(binary) - stop):
        current = int(binary[idx - 1])
        if current == 0:
            count += 1
        idx -= 1
    return count


def get_first_non_trailing_1(val: int) -> int:
    binary = f"{val:b}"
    idx = len(binary)
    first_0 = 0
    while idx:
        current = int(binary[idx - 1])
        if current == 0 and first_0 == 0:
            first_0 = idx
        if current == 1 and idx < first_0:
            return len(binary) - idx
        idx = idx - 1


def next_largest_number(integer: int) -> int:
    first_non_trailing_0_idx = get_last_non_trailing_0(integer)
    count_of_1s = count_1s(integer, first_non_trailing_0_idx)
    val_with_flipped_0 = set_at(integer, first_non_trailing_0_idx)
    val_with_cleared_1s = clear_to(val_with_flipped_0, first_non_trailing_0_idx)
    val_with_filled_1s = fill_with_1s(val_with_cleared_1s, count_of_1s - 1)
    return val_with_filled_1s


def previous_smallest_number(integer: int):
    first_non_trailing_1_idx = get_first_non_trailing_1(integer)
    count_of_0s = count_0s(integer, first_non_trailing_1_idx)
    count_of_1s = first_non_trailing_1_idx - count_of_0s
    val_with_flipped_1 = clear_at(integer, first_non_trailing_1_idx)
    val_with_cleared_1s = clear_to(val_with_flipped_1, first_non_trailing_1_idx)
    val_with_filled_1s = fill_with_1s(val_with_cleared_1s, count_of_1s + 1)
    return val_with_filled_1s


def get_last_non_trailing_0(val: int):
    binary = f"{val:b}"
    idx = len(binary)
    first_1 = 0
    while idx:
        current = int(binary[idx - 1])
        if current == 1 and first_1 == 0:
            first_1 = idx
        if current == 0 and idx < first_1:
            return len(binary) - idx
        idx = idx - 1
