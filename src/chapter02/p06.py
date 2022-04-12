from chapter02.linkedlist import LinkedList


def is_palindrome(linkedlist: LinkedList) -> bool:
    fast = slow = linkedlist.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    # cover uneven linkedlist length
    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()
        if top != slow.value:
            return False
        slow = slow.next

    return True

functions = [is_palindrome]