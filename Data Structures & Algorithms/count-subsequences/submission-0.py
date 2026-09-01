class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memory = {}
        n = len(s)
        m = len(t)
        def dfs(i, j):
            if i >= n or j >= m:
                return 0
            if (i,j) in memory:
                return memory[(i,j)]
            
            if s[i] == t[j]:
                memory[(i,j)] = dfs(i+1, j)
                memory[(i,j)] += dfs(i+1, j+1)
                if j == m-1:
                    memory[(i,j)] += 1
            else:
                memory[(i,j)] = dfs(i+1, j)
            return memory[(i,j)]
        return dfs(0,0)
