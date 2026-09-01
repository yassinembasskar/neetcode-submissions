class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        res = []
        arrow = 'right'
        while len(visited) < n*m:
            res.append(matrix[i][j])
            visited.add((i, j))
            if arrow == 'right':
                if j + 1 >= n or (i, j + 1) in visited:
                    arrow = 'down'
                if i + 1 < m and (i + 1, j) not in visited and arrow == 'down':
                    i += 1
                elif arrow == 'right':
                    j += 1
            elif arrow == 'down':
                if i + 1 >= m or (i + 1, j) in visited:
                    arrow = 'left'
                if j - 1 >= 0 and (i, j - 1) not in visited and arrow == 'left':
                    j -= 1
                elif arrow == 'down':
                    i += 1
            elif arrow == 'left':
                if j - 1 < 0 or (i, j - 1) in visited:
                    arrow = 'up'
                if i - 1 >= 0 and (i - 1, j) not in visited and arrow == 'up':
                    i -= 1
                elif arrow == 'left':
                    j -= 1
            elif arrow == 'up':
                if i - 1 < 0 or (i - 1, j) in visited:
                    arrow = 'right'
                if j + 1 < n and (i, j + 1) not in visited and arrow == 'right':
                    j += 1
                elif arrow == 'up':
                    i -= 1
        return res