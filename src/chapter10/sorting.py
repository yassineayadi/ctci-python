def swap(left: int, right: int, arr: list):
    arr[left], arr[right] = arr[right], arr[left]


def selection_sort(arr: list[int]):
    current_min, min_idx = arr[0], 0
    size = len(arr)
    next_idx = 0
    while next_idx != size:
        for i in range(next_idx, size):
            if arr[i] < current_min:
                current_min = arr[i]
                min_idx = i
        swap(next_idx, min_idx, arr)
        next_idx += 1
        current_min, min_idx = arr[min_idx], next_idx
    return arr


def bubble_sort(arr: list[int]):
    size = len(arr)

    for i in reversed(range(size)):
        for cur_idx in range(i + 1):
            if cur_idx > 0:
                prev_idx = cur_idx - 1
                if arr[cur_idx] < arr[prev_idx]:
                    swap(cur_idx, prev_idx, arr)
    return arr


def sort(arr: list[int]):
    if len(arr) == 1:
        return arr


def merge(left, right):
    merged_result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            value = left[i]
            merged_result.append(value)
            i += 1
        else:
            value = right[j]
            merged_result.append(value)
            j += 1
    while i < len(left):
        merged_result.append(left[i])
        i += 1
    while j < len(right):
        merged_result.append(right[j])
        j += 1
    return merged_result


def merge_sort(arr: list[int]):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    sorted_left, sorted_right, = merge_sort(
        left
    ), merge_sort(right)
    return merge(sorted_left, sorted_right)


def quick_sort(arr: list[int], start: int, end: int):
    pivot = end
    bigger = smaller = last_bigger = None
    i = start
    while start <= i <= end:
        current = arr[i]
        if current > arr[end] and bigger is None:
            bigger = last_bigger = i
        elif current < arr[end]:
            smaller = i
        if bigger is not None and smaller is not None and bigger < smaller:
            swap(bigger, smaller, arr)
            i = bigger
            bigger = smaller = None
        i += 1
    if last_bigger is not None:
        swap(last_bigger, pivot, arr)
        quick_sort(arr, start, last_bigger - 1)
        quick_sort(arr, last_bigger + 1, end)
    return arr
