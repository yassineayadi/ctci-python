from chapter02.linkedlist import LinkedList


def is_circular(linkedlist: LinkedList) -> bool:
    next_references = set()
    for node in linkedlist:
        if id(node) in next_references:
            return True
        else:
            next_references.add(id(node))
