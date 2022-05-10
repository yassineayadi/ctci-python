int_edges = [(0, 1), (4, 1), (1, 3), (4, 0), (3, 2)]
str_edges = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]

from chapter04.p07 import (
    topological_sort,
    create_graph_from_list_of_edges,
    topological_sort_with_arbitrary_starting_index,
    dfs_with_arbitrary_datatypes,
)


def test_topological_sort():
    graph = create_graph_from_list_of_edges(int_edges)
    order = topological_sort(graph)
    print(order)


def test_topological_sort_with_arbitrary_starting_index():
    graph = create_graph_from_list_of_edges(int_edges)
    order = topological_sort_with_arbitrary_starting_index(graph)
    print(order)


def test_dfs_with_strings_values():
    graph = create_graph_from_list_of_edges(str_edges)
    parents = dfs_with_arbitrary_datatypes(graph, "a")
    print(parents)

def test_tp_sort_with_string_values():
