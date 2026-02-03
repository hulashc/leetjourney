






# true if there is a cycle , flase if there is not

# time O(n), space O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

































class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        
        slow = slow.next
        fast = fast.next.next
    
    return True