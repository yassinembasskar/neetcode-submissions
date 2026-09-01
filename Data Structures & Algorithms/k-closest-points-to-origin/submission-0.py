class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDistance(p):
            import math
            return math.sqrt(p[0]**2+p[1]**2)
        import heapq
        heap = []
        for point in points:
            heapq.heappush(heap, (-calcDistance(point), point))
            if len(heap) > k:
                heapq.heappop(heap)
        result = [couple[1] for couple in heap]
        return result