def mergeNodes(head):
    dummy,tail = ListNode()
    total = 0
    cur = head.next
    while cur:
        if cur.val == 0:
            node = ListNode(total)
            tail.next = node
            tail = tail.next
            total = 0
        else:
            total += cur.val
        cur = cur.next
    return dummy.next
