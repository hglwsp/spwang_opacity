def reverseBetween(head, m, n):
    # 哨兵节点防止链表为空
    pre = ListNode(-1)
    pre.next = head

    for i in range(1,m):
        pre = pre.next

    cur = pre.next
    for j in range(m,n):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = pre.next
        pre.next = nxt

    return pre.next



