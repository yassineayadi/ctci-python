from chapter10.p05 import search_sorted_sparce_space


def test_search_sorted_sparce_space():
    sparce_space = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    assert (
        search_sorted_sparce_space(sparce_space, "ball", 0, len(sparce_space) - 1) == 4
    )
