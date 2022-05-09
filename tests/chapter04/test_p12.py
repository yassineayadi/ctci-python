from chapter04.p12 import (
    paths_with_sum_from_root,
    paths_with_sum_from_root_running_total,
)


def test_sum_paths(btree):
    paths = paths_with_sum_from_root(btree.root, 8)
    assert paths == 3


def test_paths_with_sum_from_root_running_total(btree):
    paths = paths_with_sum_from_root_running_total(btree.root, 8)
    assert paths == 3
