class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, visited, word):
            if word == "":
                return True
            visited.add((i,j))
            if i + 1 < len(board) and (i+1, j) not in visited and word[0] == board[i+1][j]:
                if backtrack(i+1,j,visited, word[1:]):
                    return True
            if i - 1 >= 0 and (i-1, j) not in visited and word[0] == board[i-1][j]:
                if backtrack(i-1,j,visited, word[1:]):
                    return True
            if j + 1 < len(board[0]) and (i, j+1) not in visited and word[0] == board[i][j+1]:
                if backtrack(i,j+1,visited, word[1:]):
                    return True
            if j - 1 >= 0 and (i, j-1) not in visited and word[0] == board[i][j-1]:
                if backtrack(i,j-1,visited, word[1:]):
                    return True
            visited.remove((i,j))
            return False

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, visited, word[1:]):
                        return True
        return False