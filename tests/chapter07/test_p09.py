from chapter07.p09 import CircularArray


def test_circular_array():
    circular_array = CircularArray(4)
    circular_array[0] = 0
    circular_array[1] = 1
    circular_array[2] = 2
    circular_array[3] = 3

    circle = iter(circular_array)
    for _ in [0, 1, 2, 3, 0, 2, 3]:
        next_val = next(circle)
        print(f"{next_val=}")
        assert next_val == _
