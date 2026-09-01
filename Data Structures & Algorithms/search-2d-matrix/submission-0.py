class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        while start <= end:
            mid = (start + end) // 2
            midx = mid // len(matrix[0])
            midy = mid % len(matrix[0])
            if matrix[midx][midy] < target:
                start = mid + 1
            elif matrix[midx][midy] > target:
                end = mid - 1
            else:
                return True
            
        return False