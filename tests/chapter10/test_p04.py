from chapter10.p04 import binary_search_with_unknown_size


class ArrayWithoutOfBoundReturn(list):
    def __getitem__(self, item):
        if item > len(self)-1:
            return -1
        return super().__getitem__(item)


def test_array_with_out_of_bound_return():
    array = ArrayWithoutOfBoundReturn([1, 2, 3])
    assert array[5] == -1
    assert array[2] == 3


def test_binary_search_with_unknown_size():
    array = ArrayWithoutOfBoundReturn(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    )
    assert binary_search_with_unknown_size(array, 14) == 13
    assert binary_search_with_unknown_size(array, 22) == -1
