class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memory = {}
        m = len(matrix)
        n = len(matrix[0])
        def dfs(i, j):
            cords =[(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            res = [0]
            for cord in cords:
                if cord[0] >= m or cord[1] >= n or cord[0] < 0 or cord[1] < 0:
                    continue
                if matrix[i][j] < matrix[cord[0]][cord[1]]:
                    if (cord[0],cord[1]) not in memory:
                        res.append(dfs(cord[0],cord[1]))
                    else:
                        res.append(memory[(cord[0],cord[1])])
            memory[(i,j)] = max(res)+1
            return memory[(i,j)]
        
        new_res = []
        for i in range(m):
            for j in range(n):
                if (i,j) not in memory:
                    dfs(i,j)
                new_res.append(memory[(i,j)])
        return max(new_res)
