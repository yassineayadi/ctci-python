def bfs(graph, root):  # Adj: adjacency list, s: starting vertex
    parents = [None for _ in graph]  # O(V) (use hash if unlabeled)
    # parent of root node is root
    parents[root] = root  # O(1) root
    levels = [[root]]  # O(1) initialize levels
    while len(levels[-1]) > 0:  # O(?) last level contains vertices
        levels.append([])  # O(1) amortized, make new level
        last_level = levels[-2]
        for vertex in last_level:  # O(?) loop over last full level
            for neighbour in graph[vertex]:  # O(Adj[u]) loop over neighbors
                if parents[neighbour] is None:  # O(1) parent not yet assigned
                    parents[neighbour] = vertex  # O(1) assign parent from level[-2]
                    levels[-1].append(neighbour)  # O(1) amortized, add to border
    return parents


def path_between_two_nodes(graph, start, end):
    # get list of parents
    parents = bfs(graph, start)
    # if there is no parent connecting `start`to `end` return
    if parents[end] is None:
        return

    path = []
    parent = parents[end]

    while parent != start:
        path.append(parent)
        parent = parents[parent]
    path = [start] + path + [end]

    return path
