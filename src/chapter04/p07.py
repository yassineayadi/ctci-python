# (X,Y) X, Y
# X: parent
# Y: child (depends on X)
# (a, d), (f, b), (b, d), (f, a), (d, c)
from collections import defaultdict
from typing import List, Any


def create_graph_from_list_of_edges(edges: List[tuple]):
    graph = defaultdict(list)
    for edge in edges:
        parent, child = edge
        graph[parent].append(child)
        if not graph[child]:
            graph[child] = []
    return graph


def depth_first_search(
    graph: dict,
    source: Any,
    parents: list = None,
    order: list = None,
    visited: list = None,
):
    if parents is None:
        parents = [None for _ in graph]
        order = []
        parents[source] = source

    neighbours = graph[source]

    for node in neighbours:
        if parents[node] is None:
            parents[node] = source
            depth_first_search(graph, node, parents, order, visited)
    visited[source] = True
    order.append(source)
    return parents, order


def full_dfs(graph):
    parents = [None for _ in graph]
    visited = [False for _ in graph]
    order = []
    for node in graph:
        if visited[node] is False:
            visited[node] = True
            parents[node] = node
            depth_first_search(graph, node, parents, order, visited)
    return parents, order


def topological_sort_with_arbitrary_starting_index(graph):
    parents, order = full_dfs(graph)
    return order[::-1]


def topological_sort(graph):
    parents, order = depth_first_search(graph, 4)
    return order[::-1]


def dfs_with_arbitrary_datatypes(graph: dict, source: Any, parents: dict = None):
    if parents is None:
        parents = defaultdict(lambda: None)
        parents[source] = source

    neighbours = graph[source]
    for node in neighbours:
        if parents[node] is None:
            parents[node] = source
            dfs_with_arbitrary_datatypes(graph, node, parents)
    return parents
