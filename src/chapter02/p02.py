from chapter02.linkedlist import LinkedList, Node


def get_last_element(linkedlist: LinkedList):
    for idx, node in enumerate(linkedlist):
        if node.next is None:
            return node


def get_kth_to_last_element(linkedlist: LinkedList, k: int):
    start = 1
    shift = k

    head_node = linkedlist.head
    curr_node = linkedlist.current
    kth_node = None

    while curr_node:
        if start == shift:
            kth_node = head_node
        if curr_node.next is not None:
            if kth_node:
                kth_node = kth_node.right
            curr_node = curr_node.next
            start += 1
        else:
            break
    return kth_node


def get_previous(node: Node, steps: int) -> Node:
    if node.prev is None:
        raise Exception("You arrived at the end of the Linkedlist.")
    while steps > 1:
        steps -= 1
        return get_previous(node.prev, steps)
    return node.prev


functions = [get_kth_to_last_element]
