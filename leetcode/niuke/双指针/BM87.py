def merge(A, m, B, n):
    i = m-1
    j = n-1
    p = m+n-1
    while i>=0 and j>=0:
        if A[i]>B[j]:
            A[p] = A[i]
            p-=1
            i-=1
        else:
            A[p] = B[j]
            p-=1
            j-=1
    while j>0:
        A[p] = B[j]
        p-=1
        j-=1