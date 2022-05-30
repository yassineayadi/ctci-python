from chapter10.p11 import sort_array_into_peaks_and_valleys


def test_sort_array_into_peaks_and_valleys():
    array = [5, 3, 1, 2, 3]
    assert sort_array_into_peaks_and_valleys(array) == [5, 1, 3, 2, 3]
