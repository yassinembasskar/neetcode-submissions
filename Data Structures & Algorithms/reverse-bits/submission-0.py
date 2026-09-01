class Solution:
    def reverseBits(self, n: int) -> int:
        exp1 = 31
        exp2 = 0
        rev = 0
        while n > 0:
            if 2**exp1 <= n:
                n -= 2**exp1
                rev += 2**exp2
            exp1-=1
            exp2+=1
        return rev