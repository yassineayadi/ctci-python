from chapter10.search import binary_search


def test_binary_search():
    sorted_array = [0, 1, 2, 3, 4, 5, 6, 7]
    assert binary_search(sorted_array, 2) == 2
    sorted_array = [0, 1, 2, 5, 10]
    assert binary_search(sorted_array, 5) == 3
    assert binary_search(sorted_array, 15) == -1
