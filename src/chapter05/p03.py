def flip_bit_to_win(number: int):
    binary = f"{number:b}"
    idx = len(binary)
    longest_segment = 0
    current_segment = 0
    zero_interruption = 0
    while idx:
        current = int(binary[idx - 1])
        if current == 1:
            current_segment += 1
        elif current == 0:
            if zero_interruption == 0:
                zero_interruption += 1
                longest_segment = max(longest_segment, current_segment)
            else:
                longest_segment = max(longest_segment, current_segment)
                current_segment = 0
                zero_interruption = 0
        idx -= 1
    longest_segment = longest_segment + 1
    return longest_segment
