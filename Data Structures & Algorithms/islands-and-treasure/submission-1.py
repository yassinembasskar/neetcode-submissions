class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        queue = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        while queue:
            i, j = queue.popleft()
            for couple in [(i, j-1), (i, j+1), (i+1, j), (i-1, j)]:
                if couple[0] < 0 or couple[1] < 0 or couple[0] > len(grid) - 1 or couple[1] > len(grid[0]) -1 or grid[couple[0]][couple[1]] == -1 or couple in visited:
                    continue
                grid[couple[0]][couple[1]] = grid[i][j]+1
                queue.append(couple)
                visited.add(couple)                