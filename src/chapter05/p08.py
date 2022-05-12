from typing import List


def get_height(width: int, point: int):
    return point // width


def binary_form(screen: List[int]):
    return " ".join(f"{byte:0>8b}" for byte in screen)


class DrawError(Exception):
    pass


def draw_line(screen: list, source: int, target: int, width: int, height: int):
    if target > width:
        raise DrawError(
            f"Target {target} outside of screen (Width={width}). Cannot draw horizontal line."
        )

    source_byte = (
        (width * height) + source
    ) // 8  # source byte position in screen array
    target_byte = (
        (width * height) + target
    ) // 8  # target byte position in screen array
    start_offset = source % 8
    end_offset = target % 8
    first_full_byte = source_byte if start_offset == 0 else source_byte + 1
    last_full_byte = target_byte if end_offset == 7 else target_byte - 1

    if first_full_byte <= last_full_byte:
        for b in range(first_full_byte, last_full_byte + 1):
            screen[b] = 0xFF

    start_mask = (1 << (7 - start_offset + 1)) - 1
    end_mask = (0xFF << (7 - end_offset)) & 0xFF

    if source_byte == target_byte:
        screen[source_byte] = start_mask & end_mask
    else:
        screen[source_byte] = start_mask
        screen[target_byte] = end_mask
    return screen
