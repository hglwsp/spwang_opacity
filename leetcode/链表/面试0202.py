def kthToLast(head, k):
    # len = 0
    # h = head
    # while h:
    #     h = h.next
    #     len+=1
    # h = head  # 重新指向
    # while len - k + 1> 0:
    #     h = h.next
    # return h.val
    fast,slow = head,head
    while k > 0:  #快指针先走
        fast = fast.next
        k -= 1
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.val