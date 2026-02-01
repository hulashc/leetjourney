


# iterative method o(1) space , o(m+n) time

def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Attach remaining nodes
    tail.next = list1 if list1 else list2

    return dummy.next

# recursive solutions

def merge_two_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists(list1, list2.next)
        return list2
