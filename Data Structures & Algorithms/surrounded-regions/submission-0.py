class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows = len(board)
        cols = len(board[0])
        def backtrack(i, j, visited):
            if i < 0 or j < 0 or i > rows-1 or j > cols-1:
                return
            if board[i][j] == "X":
                return 
            if (i, j) in visited:
                return
            visited.add((i,j))
            backtrack(i+1, j, visited)
            backtrack(i-1, j, visited)
            backtrack(i, j+1, visited)
            backtrack(i, j-1, visited)
        
        for i in range(rows):
            backtrack(i, cols-1, visited)
            backtrack(i, 0, visited)
        for j in range(cols):
            backtrack(rows-1, j, visited)
            backtrack(0, j, visited)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
        