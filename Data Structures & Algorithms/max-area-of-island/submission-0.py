class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        counter = 0
        def backtrack(i, j):
            counter = 0
            if grid[i][j] == 1:
                visited.add((i,j))
                counter+=1
                for item in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if item in visited or item[0] > len(grid) - 1 or item[1] > len(grid[0]) - 1 or item[0] < 0 or item[1] < 0:
                        continue
                    elif grid[item[0]][item[1]] == 1:
                        counter += backtrack(item[0],item[1])
            return counter
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    counter = max(counter, backtrack(i, j))
        return counter