class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory = {}
        def dfs(i, j):
            if i > m or j > n:
                return 0
            elif i == m and j == n:
                return 1
            if (i, j) in memory:
                return memory[(i,j)]
            
            result = dfs(i+1, j) + dfs(i, j+1)
            memory[(i,j)] = result
            return result
        return dfs(1, 1)