def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    flagA = headA
    flagB = headB
    lenA,lenB = 0,0
    while flagA:
        lenA+=1
        flagA = flagA.next
    while flagB:
        lenB+=1
        flagB = flagB.next
    flagA, flagB = headA, headB
    if lenA >= lenB:
        d = lenA - lenB
        while d > 0:
            flagA = flagA.next
            d-=1
    else:
        d = lenB - lenA
        while d > 0:
            flagB = flagB.next
            d-=1
    while flagA:
        if flagA == flagB:
            return flagA
        else:
            flagA = flagA.next
            flagB = flagB.next
    return None
