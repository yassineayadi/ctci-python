from chapter02.linkedlist import LinkedList


def get_middle_node(linkedlist: LinkedList):
    current_node = linkedlist.current
    runner_node = current_node.next
    while current_node:
        if runner_node.next is not None:
            runner_node = runner_node.next.next
            current_node = current_node.next
        else:
            break
    return current_node.value


functions = [get_middle_node]
