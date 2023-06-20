def reversePrint(head):
    if not head:
        return []

    pre = None
    cur = head
    len = 0
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
        len += 1
    res = [0]*len
    i=0
    while pre:
        res[i] = pre.val
        i+=1
        pre = pre.next
    return res
