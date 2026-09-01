class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -x
        exp2 = len(str(x)) - 1
        out = 0
        while exp2 >= 0:
            out+= (x % 10) * 10**exp2
            x = x // 10
            exp2-=1
        if neg:
            out = -out
        if out < -2**31 or out >= 2**31:
            return 0
        return out