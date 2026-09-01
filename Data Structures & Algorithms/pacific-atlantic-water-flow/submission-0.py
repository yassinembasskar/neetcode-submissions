class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificSet = set()
        atlanticSet = set()
        def backtrack(i, j, pacific, atlantic):
            if pacific:
                pacificSet.add((i, j))
            if atlantic:
                atlanticSet.add((i,j))
            for ii, jj in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                if ii < 0 or jj < 0 or ii > len(heights)-1 or jj > len(heights[0])-1:
                    continue
                if heights[i][j] <= heights[ii][jj]:
                    if ((ii, jj) not in pacificSet and pacific) or ((ii, jj) not in atlanticSet and atlantic):
                        backtrack(ii, jj, pacific, atlantic)
        
        result = []
        n = len(heights)
        m = len(heights[0])
        for i in range(n):
            backtrack(i, 0, True, False)
            backtrack(i, m-1, False, True)
        for j in range(m):
            backtrack(0, j, True, False)
            backtrack(n-1, j, False, True)
        for i in range(n):
            for j in range(m):
                if (i, j) in pacificSet and (i, j) in atlanticSet:
                    result.append([i, j])
        return result