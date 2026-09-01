class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memory = {}
        m = len(s1)
        n = len(s2)
        if len(s3) != n+m:
            return False
        def dp(i, j, current):
            if (i,j,current) in memory:
                return memory[(i,j,current)]
            if i >= m and j >= n:
                return True
            if i >=m:
                while j < n:
                    if s2[j] != s3[current]:
                        return False
                    j+=1
                    current+=1
                return True
            elif j>=n:
                while i < m:
                    if s1[i] != s3[current]:
                        return False
                    i+=1
                    current+=1
                return True
            
            if s1[i] != s3[current] and s2[j]!=s3[current]:
                memory[(i,j,current)] = False
                return False
            left = False
            right = False
            if s1[i]==s3[current]:
                left = dp(i+1, j, current+1)
            if s2[j]==s3[i+j]:
                right = dp(i, j+1, current+1)
            memory[(i,j,current)] = left or right
            return left or right
        return dp(0,0,0)
