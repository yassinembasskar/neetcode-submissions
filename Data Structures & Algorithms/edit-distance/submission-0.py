class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memory = {}
        n = len(word1)
        m = len(word2)
        def dfs(i, j):
            if (i, j) in memory:
                return memory[(i, j)]
            if i >= n and j >= m:
                return 0
            if j >= m:
                memory[(i,j)] = 1 + dfs(i+1, j)
                return memory[(i,j)]
            if i >= n:
                memory[(i,j)] = 1 + dfs(i, j+1)
                return memory[(i,j)]
            
            if word1[i] != word2[j]:
                run1 = dfs(i, j+1)
                run2 = dfs(i+1, j)
                run3 = dfs(i+1, j+1)
                memory[(i,j)] = 1 + min(run1, run2, run3)
            else:
                memory[(i,j)] = dfs(i+1, j+1)
            return memory[(i,j)]

        return dfs(0,0)