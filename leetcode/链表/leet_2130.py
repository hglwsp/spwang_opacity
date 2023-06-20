def pairSum(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 反转链表
    pre = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    ans = 0
    x = head
    y = pre
    while pre:
        ans = max(x.val+y.val,ans)
        x = x.next
        y = y.next
    return ans


