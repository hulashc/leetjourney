

# optimal solutions O(1) space, O(n) time

def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# hashset

def has_cycle(head):
    seen = set()

    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next

    return False
