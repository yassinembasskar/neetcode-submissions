class Solution:
    def hammingWeight(self, n: int) -> int:
        exp = 31
        counter = 0
        while exp >= 0:
            if 2**exp <= n:
                n = n-2**exp
                counter+=1
            exp-=1
        return counter