class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memory = {}
        m = len(s1)
        n = len(s2)
        if len(s3) != n+m:
            return False
        def dp(i, j, current):
            if (i,j) in memory:
                return memory[(i,j)]
            if i >= m and j >= n:
                return True

            isInter = False
            if i<m and s1[i]==s3[current] and dp(i+1, j, current+1):
                isInter = True
            elif j<n and s2[j]==s3[i+j] and dp(i, j+1, current+1):
                isInter = True
            memory[(i,j)] = isInter
            return isInter
        return dp(0,0,0)
