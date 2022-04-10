from chapter02.linkedlist import LinkedList, Node


def partition_linkedlist(linkedlist: LinkedList, partition: int) -> LinkedList:
    partition_node = Node(value=partition)
    new_list = LinkedList(partition_node)
    for node in linkedlist:
        if node < partition_node:
            new_list.add_before(partition_node, node)
        elif node >= partition_node:
            new_list.add_after(partition_node, node)
    return new_list


functions = [partition_linkedlist]