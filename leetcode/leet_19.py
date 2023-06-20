def removeNthFromEnd(head, n):
    dummy = ListNode(-1)
    dummy.next = head
    # 双指针
    slow = dummy
    fast = dummy
    # fast 先走 n steps
    while n > 0:
        fast = fast.next
        n-=1
    # slow, fast 同时走, fast 到达尾结点
    while fast.next:
        slow = slow.next
        fast = fast.next
    # slow.next 是要删除的节点
    slow.next = slow.next.next
    return dummy.next