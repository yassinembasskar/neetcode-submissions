class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificSet = set()
        atlanticSet = set()
        rows = len(heights)
        cols = len(heights[0])
        def backtrack(i, j, visited, prev_height):
            if i < 0 or j < 0 or i > rows-1 or j > cols-1:
                return
            if (i, j) in visited:
                return
            if heights[i][j] < prev_height:
                return
            visited.add((i, j))
            for ii, jj in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                backtrack(ii, jj, visited, heights[i][j])
        
        
        for i in range(rows):
            backtrack(i, 0, pacificSet, heights[i][0])
            backtrack(i, cols-1, atlanticSet, heights[i][cols-1])
        for j in range(cols):
            backtrack(0, j, pacificSet, heights[0][j])
            backtrack(rows-1, j, atlanticSet, heights[rows-1][j])

        return [[i, j] for i, j in pacificSet if (i, j) in atlanticSet]