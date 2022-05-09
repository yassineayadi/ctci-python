from collections import defaultdict

from chapter04.trees import BinaryNode


def paths_with_sum_from_node(
    node: BinaryNode, target: int, current_sum: int, matching_paths: int
):
    if node is None:
        return matching_paths
    current_sum += node.data
    if current_sum == target:
        matching_paths += 1

    matching_paths = paths_with_sum_from_node(
        node.left, target, current_sum, matching_paths
    )
    matching_paths = paths_with_sum_from_node(
        node.right, target, current_sum, matching_paths
    )
    return matching_paths


def paths_with_sum_from_root(current: BinaryNode, target: int) -> int:
    if current is None:
        return 0
    current_sum = 0
    matching_paths = 0
    paths_from_root = paths_with_sum_from_node(
        current, target, matching_paths, current_sum
    )
    paths_from_left = paths_with_sum_from_root(current.left, target)
    paths_from_right = paths_with_sum_from_root(current.right, target)

    return paths_from_root + paths_from_left + paths_from_right


def paths_with_sum_from_node_running_total(
    current: BinaryNode, target, running=None, hashtable: dict = None
):
    hashtable = defaultdict(lambda: 0) if not hashtable else hashtable
    if not current:
        return 0
    running += current.data
    total = hashtable[running - target]
    if running == target:
        total += 1
    hashtable[running] += 1
    total += paths_with_sum_from_node_running_total(
        current.left, target, running, hashtable
    )
    total += paths_with_sum_from_node_running_total(
        current.right, target, running, hashtable
    )
    hashtable[running] -= 1
    return total


def paths_with_sum_from_root_running_total(current: BinaryNode, target: int):
    total = paths_with_sum_from_node_running_total(current, target, 0)
    return total
