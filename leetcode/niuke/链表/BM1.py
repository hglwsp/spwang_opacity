def ReverseList(head):
    if not head:
        return []
    if head.next == null:
        return head
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre