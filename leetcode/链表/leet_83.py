# def deleteDuplicates(head):
#     if not head:
#         return head
#     h = head
#     while h.next:
#         if h.val == h.next.val:
#             h.next = h.next.next
#         else:
#             h = h.next
#     return head

def createNode(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


def listsort(head):
    if not head:
        return head
    l = 0   # len of list
    nums1 = []
    h = head
    while h.bext:
        l += 1
        h = h.next
        nums1.append(h.val)               #链表->数组
    nums21,nums22 = [0]*(l//2),[0]*(l//2)     # 分别获取idx 奇数和偶数
    for i in range(0,l//2):                  # 偶数
        nums21[i] = nums1[2*i]
    for i in range(0,l//2-1):             #奇数
        nums22[i] = nums1[2 * i+1]
    N = len(nums22)
    for i in range(int(len(nums22) / 2)):        # 逆序
        nums22[i], nums22[N - i - 1] = nums22[N - i - 1], nums22[i]
    nums21.append(nums22)
    nums_deal = nums21                 # 数组
    createNode(nums_deal)             # 数组->链表