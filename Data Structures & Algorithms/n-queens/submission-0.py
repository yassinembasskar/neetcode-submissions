class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(i, j, visited):
            if i == n:
                res.append(visited[:])
                return
            if j == n:
                return 

            for v in visited:
                if v[1] == j or v[0] - i == v[1] - j or v[0] + v[1] == i + j:
                    backtrack(i, j+1, visited)
                    return
                    
            visited.append((i, j))
            backtrack(i+1, 0, visited)
            visited.pop(-1)
            backtrack(i, j+1, visited)

        
        backtrack(0, 0, [])

        new_res = []
        for r in res:
            new_res.append([])
            for item in r:
                chars = ['.'] * n
                chars[item[1]] = "Q"
                new_res[-1].append(''.join(chars))

        return new_res
