class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        import heapq
        graph = {}
        prices = {}
        for flight in flights:
            if flight[0] not in graph:
                graph[flight[0]] = set()
            graph[flight[0]].add(flight[1])
            prices[(flight[0], flight[1])] = flight[2]
        
        queue = []
        heapq.heappush(queue, (0, -1, src, dst))
        visited = set()
        while queue:
            price, stops, source, distination = heapq.heappop(queue)
            if (stops, source) in visited:
                continue
            visited.add((stops, source))
            if source == distination and stops <= k:
                return price
            if source not in graph or stops > k:
                continue
            for mid in graph[source]:
                new_price = price + prices[(source, mid)]
                if (stops+1, mid) not in visited:  
                    heapq.heappush(queue, (new_price, stops+1, mid, distination))
        return -1