from chapter02.linkedlist import LinkedList


def sum_two_linkedlists(left: LinkedList, right: LinkedList):
    new_list = LinkedList()
    carry = 0
    n1, n2 = left.head, right.head

    while n1 or n2:
        result = carry

        if getattr(n1, "value", None) is not None:
            result += n1.value

        if getattr(n2, "value", None) is not None:
            result += n2.value

        new_list.add(result % 10)
        carry = result // 10

        n1 = n1.next if hasattr(n1, "next") else None
        n2 = n2.next if hasattr(n2, "next") else None
        # , n2.next

    return new_list


functions = []
