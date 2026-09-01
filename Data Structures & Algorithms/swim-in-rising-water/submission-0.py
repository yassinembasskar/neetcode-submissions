class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        n = len(grid)
        queue = []
        heapq.heappush(queue, (grid[0][0], 0, 0))
        visited = set()
        while queue:
            dist, i, j = heapq.heappop(queue)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == n-1 and j == n-1:
                return dist
            directions = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
            for c_i, c_j in directions:
                if (c_i, c_j) in visited or c_i < 0 or c_j < 0 or c_i > n-1 or c_j > n-1:
                    continue
                new_dist = max(dist, grid[c_i][c_j])
                heapq.heappush(queue, (new_dist, c_i, c_j))
        
