def isPail(head):
    # special
    if not head:
        return True
    slow, fast = head,head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 反转后半部分链表
    pre = None
    cur = slow.next
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    while pre:
        if pre.val != head.val:
            return False
        else:
            pre = pre.next
            head = head.next
    return True