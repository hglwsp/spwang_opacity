def reverseList(head):
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre