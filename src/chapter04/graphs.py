def dfs_recursive(
    graph: dict,
    starting_node: str,
    path: list = None,
):
    path = [] if path is None else path
    path.extend(starting_node)
    for node in graph[starting_node]:
        if node not in path:
            path = dfs_recursive(graph, node, path)
    return path


def dfs_non_recursive(graph: dict, starting_node: str):
    path = []
    stack = [starting_node]

    while stack:
        node = stack.pop()
        if node in path:
            continue
        path.append(node)
        for neighbour in graph[node]:
            stack.append(neighbour)

    return path


def bfs_non_recursive(graph: dict, starting_node: str):
    queue = [starting_node]
    visited_nodes = {starting_node}
    path = [starting_node]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited_nodes:
                visited_nodes.add(neighbour)
                queue.append(neighbour)
                path.append(neighbour)
    return path


def bfs_generator(graph: dict, starting_node: str) -> list:
    queue = [starting_node]
    visited_nodes = {starting_node}
    path = [starting_node]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited_nodes:
                visited_nodes.add(neighbour)
                queue.append(neighbour)
                path.append(neighbour)
        yield path
    return path


def bfs_sp(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting path doesn't exist :(")
    return