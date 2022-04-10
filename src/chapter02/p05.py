from chapter02.linkedlist import LinkedList


def sum_two_linkedlists(left: LinkedList, right: LinkedList):
    new_list = LinkedList()
    carry = 0
    n1, n2 = left.head, right.head

    while n1 or n2:
        result = carry

        if n1.value is not None:
            result += n1.value

        if n2.value is not None:
            result += n2.value

        new_list.add(result % 10)
        carry = result // 10

        n1, n2 = n1.next, n2.next

    return new_list


functions = []