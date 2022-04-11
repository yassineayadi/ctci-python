def is_substring(left: str, right: str) -> bool:
    double_right = right * 2

    if len(left) != len(right):
        return False

    if left not in double_right:
        return False

    start, *_ = double_right.split(sep=left)
    shift = len(start)

    for left_idx, left_value in enumerate(left):
        right_idx = (left_idx + shift) % len(left)
        right_value = right[right_idx]
        if left_value != right_value:
            return False
    return True


functions = [is_substring]
