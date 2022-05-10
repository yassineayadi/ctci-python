from chapter04.trees import BinarySearchNode


def get_sequence(node: BinarySearchNode):
    if node is None:
        return [[]]
    right_sequence = get_sequence(node.right)
    left_sequence = get_sequence(node.left)
    sequences = []
    for right in right_sequence:
        for left in left_sequence:
            sequences = weave(right, left, prefix=[node.data], results=sequences)
    return sequences


def weave(first: list, second: list, prefix: list, results: list):
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results
    head = first[0]
    prefix.append(head)
    results = weave(first[1:], second, prefix, results)
    prefix.pop()
    head = second[0]
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    return results
