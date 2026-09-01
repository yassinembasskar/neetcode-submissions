class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        def backtrack(i, j):
            if i < 0 or j < 0 or i > rows-1 or j > cols-1:
                return
            if board[i][j] != "O":
                return 

            board[i][j] = "V"
            backtrack(i+1, j)
            backtrack(i-1, j)
            backtrack(i, j+1)
            backtrack(i, j-1)
        
        for i in range(rows):
            backtrack(i, cols-1)
            backtrack(i, 0)
        for j in range(cols):
            backtrack(rows-1, j)
            backtrack(0, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                elif board[i][j] == "O":
                    board[i][j] = 'X'
        