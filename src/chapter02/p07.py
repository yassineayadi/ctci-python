from chapter02.linkedlist import LinkedList


def has_intersection(left: LinkedList, right: LinkedList):
    if len(left) > len(right):
        longest = left
        shortest = right
    else:
        longest = right
        shortest = left

    start_idx = len(longest) - len(shortest)
    head_longest, head_shortest = longest.head, shortest.head

    for i in range(start_idx):
        head_longest = head_longest.next

    while head_longest and head_shortest:
        if (
            head_longest.value == head_shortest.value
            and head_longest.next == head_shortest.next
        ):
            return True
        head_longest = head_longest.next
        head_shortest = head_shortest.next

    return False
