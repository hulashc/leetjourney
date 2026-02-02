


# fast and slow two pointer 

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head

    fast = slow = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Remove the nth node
    slow.next = slow.next.next

    return dummy.next
