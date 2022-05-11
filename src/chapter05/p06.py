def count_1s(number: int) -> int:
    binary = f"{number:b}"
    count = 0
    for v in binary:
        if int(v) == 1:
            count += 1
    return count


def get_numbers_of_bits_to_convert(left: int, right: int):
    ox_or_mask = left ^ right
    return count_1s(ox_or_mask)
