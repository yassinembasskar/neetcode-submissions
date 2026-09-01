class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                tmp1 = matrix[j][n-1-i]
                tmp2 = matrix[n-1-i][n-1-j]
                tmp3 = matrix[n-1-j][i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[n-1-i][n-1-j] = tmp1
                matrix[n-1-j][i] = tmp2
                matrix[i][j] = tmp3
