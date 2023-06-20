def hanota(self,A, B, C):
    n = len(A)
    self.move(self,n,A,B,C)

def move(self, n, hfrom, hother, hto):
    if n==1:   # 最小问题
        hto.append(hfrom[-1])
        hfrom.pop()
        return
    else:
        self.move(n-1,hfrom,hto,hother)    #  上面n-1个移动到中间
        self.move(1,hfrom,hother,hto)     # 第n个移动到目标
        self.move(n-1,hother,hfrom,hto)   # n-1个移动到目标