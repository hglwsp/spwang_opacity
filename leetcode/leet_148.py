def sortList(self,head):
    if not head or not head.next:
        return head
    slow,fast = head,head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid,slow.next = slow.next,None
    left,right = self.sortList(head), self.sortList(mid)
    # merge
    h = res = ListNode(0)
    while left and right:
        if left.val < right.val:
            h.next = left
            left = left.next
        else:
            h.next = right
            right = right.next
        h = h.next
    if left:h.next = left
    if right:h.next = right
    return res.next