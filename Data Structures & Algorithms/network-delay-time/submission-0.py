class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        directions = {}
        for time in times:
            if time[0] not in directions:
                directions[time[0]] = []
            directions[time[0]].append((time[2],time[1]))
        
        import heapq
        heap = [(0, k)]
        visited = set()
        max_time = 0
        while heap:
            item = heapq.heappop(heap)
            if  item[1] in visited:
                continue
            visited.add(item[1])
            if item[1] not in directions:
                max_time = max(max_time, item[0])
                continue
            for c in directions[item[1]]:
                if c not in visited:
                    new_item = (item[0] + c[0], c[1])
                    heapq.heappush(heap, new_item)
            max_time = max(max_time, item[0])
        if len(visited) < n:
            return -1
        return max_time
            