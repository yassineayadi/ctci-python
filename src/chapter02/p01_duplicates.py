from chapter02.linkedlist import LinkedList


def remove_duplicates(linkedlist: LinkedList) -> LinkedList:
    seen = set()
    current = linkedlist.current
    while getattr(current, "value", None):
        if current.value in seen:
            node = current
            current = node.next
            node.delete()
        else:
            seen.add(current.value)
            current = current.next
    return linkedlist


functions = [remove_duplicates]
