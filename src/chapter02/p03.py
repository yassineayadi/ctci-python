from chapter02.linkedlist import LinkedList


def get_middle_node(linkedlist: LinkedList):
    current_node = linkedlist.current
    runner_node = current_node.right
    while current_node:
        if runner_node.right is not None:
            runner_node = runner_node.right.right
            current_node = current_node.right
        else:
            break
    return current_node.value


functions = [get_middle_node]
