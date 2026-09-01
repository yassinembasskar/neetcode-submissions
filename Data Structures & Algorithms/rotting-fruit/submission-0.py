class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        stack = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    stack.append((i,j))
        n = len(stack)
        res = 0
        while stack:
            i, j = stack.popleft()
            for ii, jj in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
                if ii < 0 or jj < 0 or ii > len(grid)-1 or jj > len(grid[0])-1 or grid[ii][jj] == 0 or grid[ii][jj] == 2:
                    continue
                grid[ii][jj] = 2
                stack.append((ii, jj))
            n-=1 
            if n == 0:
                n = len(stack)
                if n > 0:    
                    res += 1
                    
        for line in grid:
            if 1 in set(line):
                return-1
        return res