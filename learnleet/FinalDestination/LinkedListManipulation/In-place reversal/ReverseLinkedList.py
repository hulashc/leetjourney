





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next #store next
        curr.next = prev #reverse pointer
        prev = curr #move prev
        curr = next_node #move curr

    return prev