def binary_search(arr: list[int], key: int, start: int = 0, end: int = 4):
    if start > end:
        return -1
    midpoint = (end + start) // 2
    if midpoint > end:
        return -1
    if key == arr[midpoint]:
        return midpoint
    if key > arr[midpoint]:
        return binary_search(arr, key, midpoint + 1, end)
    elif key < arr[midpoint]:
        return binary_search(arr, key, start, midpoint - 1)
