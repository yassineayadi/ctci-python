from chapter04.p01 import path_between_two_nodes


def test_path_between_two_nodes(adjacency_list):
    assert path_between_two_nodes(adjacency_list, 1, 4) == [1, 2, 4]


def test_path_between_two_nodes_not_exist(adjacency_list):
    assert path_between_two_nodes(adjacency_list, 9, 2) is None


def test_bfs_shortest_path(adjacency_list):
    path = path_between_two_nodes(adjacency_list, 1, 4)
    print(path)
