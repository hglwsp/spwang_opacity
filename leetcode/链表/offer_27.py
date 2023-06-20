def isPalindrome(head):
    if head == None or head.next == None:
        return True

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # reverse
    pre = None
    cur = slow.next
    while cur:
        nxt = cur
        cur.next = pre
        pre = cur
        cur = nxt
    # compare
    while pre:
        if head.val != pre.val:
            return False
        else:
            head = head.next
            pre = pre.next
    return True