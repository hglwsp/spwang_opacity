def reverseList(head):
    if not head:
        return None
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return cur
