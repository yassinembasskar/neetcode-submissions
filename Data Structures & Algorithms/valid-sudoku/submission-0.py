class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        carre = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        lines = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        columns = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                if val in lines[i]:
                    print("here lines")
                    return False
                if val in columns[j]:
                    print("here columns")
                    return False
                if val in carre[(int(j/3)) + (int(i/3))*3]:
                    return False
                lines[i][val] = 1
                columns[j][val] = 1
                carre[(int(j/3)) + (int(i/3))*3][val] = 1

        return True