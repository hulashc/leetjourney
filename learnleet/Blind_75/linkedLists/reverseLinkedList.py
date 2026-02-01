
# Iterative approach

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # store next
        curr.next = prev       # reverse pointer
        prev = curr            # move prev
        curr = next_node       # move curr

    return prev


# recursive approach

def reverse_list(head):
    if not head or not head.next:
        return head

    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None

    return new_head
