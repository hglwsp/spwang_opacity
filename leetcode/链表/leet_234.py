def isPalindrome(head):
    if not head:
        return True
    fast = head
    slow = head
    while fast.next and fast.next.next:   # 0 0 0 0 0 1 0   -> fast move 1 end loop
        slow = slow.next
        fast = fast.next.next

    # reverse
    pre = None
    cur = slow.next
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    while pre:
        if head.val != pre.val:
            return False
        else:
            head = head.next
            pre = pre.next
    return True


