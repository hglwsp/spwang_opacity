def FindKthToTail(pHead, k):
    slow,fast = pHead,pHead
    while k:
        if not fast:
            return None
        fast = fast.next
        k-=1
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.next